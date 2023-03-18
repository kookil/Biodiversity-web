import json
from flask import Flask
from flask import request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import parse_qs
import pymysql
import os
import pandas as pd
import geopandas as gpd
import numpy as np


def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response


app = Flask(__name__)
app.after_request(after_request)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:X166d000o649l_phin@127.0.0.1:3306/biodiversity01"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "uwgf239(2@*tg8<:fiwuqfijqsjnib2"  # 自定义密钥

db = SQLAlchemy(app)  # 实例化一个mysql数据库


class SpeciesInfo(db.Model):
    id = db.Column('species_info', db.Integer, primary_key=True)
    num = db.Column(db.Integer, nullable=False)
    name_en = db.Column(db.String(30), nullable=False)
    name_ch = db.Column(db.String(30), nullable=True)
    grade = db.Column(db.String(4), nullable=True)
    type = db.Column(db.String(30), nullable=True)
    region = db.Column(db.String(1000), nullable=True)
    intro = db.Column(db.String(5000), nullable=True)
    # geojson is too big to show in cmd terminal
    # but is able to query use flask_sqlalchemy
    geojson = db.Column(db.JSON, nullable=True)
    photo = db.Column(db.String(100), nullable=True)

    def __init__(self, num, name_en, name_ch, grade, type, region, intro, geojson, photo):
        self.num = num
        self.name_en = name_en
        self.name_ch = name_ch
        self.grade = grade
        self.type = type
        self.region = region
        self.intro = intro
        self.geojson = geojson
        self.photo = photo


def to_front(data):
    return {"data": data}


@app.route("/")
def hello_world():
    return "test succeed."


@app.route('/query_region', methods=['GET', 'POST'])
def query_region():
    json_path = 'static/geojson'
    data = request.get_data()
    params = parse_qs(data, True)
    species_name = params["species_name".encode('utf-8')][0].decode()

    # files = os.listdir(json_path)
    # if f'{species_name}.json' not in files:
    #     return 'failed'
    # with open(json_path + f'/{species_name}.json', 'r', encoding='utf8') as fp:
    #     geojson = json.load(fp)

    # or SpeciesInfo.name_ch == species_name
    record = SpeciesInfo.query.filter(SpeciesInfo.name_en == species_name).first()
    if record:
        geojson = record.geojson
        if geojson:
            return to_front(geojson)
        else:
            return 'failed'
    else:
        return 'failed'


@app.route('/query_species_info_data', methods=['GET', 'POST'])
def query_species_info_data():
    data = request.get_data()
    params = parse_qs(data, True)
    species_name = params["species_name".encode('utf-8')][0].decode()

    # or SpeciesInfo.name_ch == species_name
    info_data = None
    record = SpeciesInfo.query.filter(SpeciesInfo.name_en == species_name).first()
    if record:
        info_list = [
            {'col_name': '学名', 'col_content': record.name_en},
            {'col_name': '中文名', 'col_content': record.name_ch},
            {'col_name': '威胁排序', 'col_content': record.num},
            {'col_name': '濒危等级', 'col_content': record.grade},
            {'col_name': '界', 'col_content': record.type},
            {'col_name': '分布范围', 'col_content': record.region},
            {'col_name': '物种简介', 'col_content': record.intro}
        ]
        info_data = {'photo': record.photo, 'info': info_list}
    else:
        info_data = {'photo': 'No Image.png', 'info': []}
    return to_front(info_data)


@app.route('/query_national_list', methods=['GET', 'POST'])
def query_national_list():
    excel_path = 'static/excel/National Endergered Species List.xlsx'
    df = pd.read_excel(excel_path)
    df = df.to_json(orient='records', force_ascii=False)
    return to_front(json.loads(df))


@app.route('/query_provincial_list', methods=['GET', 'POST'])
def query_provincial_list():
    excel_path = 'static/excel/Provincial Endergered Species List.xlsx'
    df = pd.read_excel(excel_path)
    data = request.get_data()
    params = parse_qs(data, True)
    province = params["province".encode('utf-8')][0].decode()
    tdf = df[[province, f'{province} species', f'{province} species type']]
    tdf.columns = ['latin_name', 'ch_name', 'kingdom']
    tdf['num'] = tdf.index.values + 1
    tdf = tdf[['num', 'latin_name', 'ch_name', 'kingdom']]
    tdf = tdf.to_json(orient='records', force_ascii=False)
    return to_front(json.loads(tdf))


if __name__ == '__main__':
    CORS(app, supports_credentials=True)
    app.run(host='127.0.0.1', port=5010, debug=False)
