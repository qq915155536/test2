#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/12/2 10:52
# Author :A0025-江苏-小丹
# QQ:915155536
# File :deploy.py
#  ===========================
import requests
import time
from ERP.login import login
from ERP.log.my_log import my_log
from ERP.conf.db import DB

# 生成日志

logger = my_log()
info_dict = {}


# 2.生成单据编号（调拨申请单号SDPR）
def test_02():
    # 1)拼接接口url
    url = info_dict['conf_url'] + 'masterdata/v1/billCodeRule/billCode/?billType=STOCK_DEPLOY_REQUEST'
    # 2）请求接口，获取调拨申请单号
    res = requests.post(url=url, headers=info_dict['base_headers'])
    # 3）接口返回数据处理
    billcode = res.json()['data']
    logger.info('生成单据编号：{}成功！'.format(billcode))
    info_dict['billCode'] = billcode
    return info_dict


# 3.新增FBA调拨申请单
def test_03():
    # 1)拼接接口url
    url = info_dict['conf_url'] + 'stockdata/v1/stockDeployRequest/insert'
    # 2)接口参数（调拨sku信息）
    if info_dict['conf'] == 'dev':
        # ①FBA调拨（1种sku（ST0684RD0M）2件）
        data_fba = {
            "mainForm": {
                "reqDeployNumber": 2,
                "billCode": info_dict['billCode'],
                "billDate": "2021-10-06T06:35:55.668Z",
                "isNeedBox": True,
                "isFixSku": None,
                "isTransferTemp": False,
                "relationshipCode": None,
                "isRelatedDeploy": False,
                "fbaWarehouseShortCode": "CS-0066",
                "receivePersonZipcode": "562762",
                "receivePersonCountryId": 178,
                "receivePersonCountry": "中国",
                "logistRequirement": 400,
                "fbaSenderAddress": "Yuhang Hangzhou Zhejiang Province",
                "fbaReceiverAddress": "马德里库里斯班144号",
                "fbaReceiverAddressId": 195,
                "applyPerson": None,
                "applyPersonId": 1913,
                "applyPersonName": "黄丹1",
                "companyId": 10,
                "bcId": 1,
                "companyName": "ZIBUYU INTERNATIONAL LIMITED",
                "companyCode": "0010",
                "deployOutWarehouseId": 26,
                "deployOutWarehouseCode": "026",
                "deployOutWarehouseName": "杭州五洲仓",
                "deployInWarehouseId": 11,
                "deployInWarehouseCode": "011",
                "deployInWarehouseName": "FBA仓",
                "status": 100,
                "creator": None,
                "reqDeployAmount": "54.27",
                "actDeployNumber": None,
                "deployBillCode": None,
                "auditor": None,
                "storeIdList": [
                    5
                ],
                "storeId": 5,
                "storeName": "WISH金鑫icen3",
                "remark": "测试数据-黄丹---FBA调拨",
                "store": None,
                "mainIds": [],
                "totalWeight": 40,
                "marketId": 4,
                "marketName": "美国站",
                "marketCode": "ATVPDKIKX0DER",
                "finalWarehouse": None,
                "adjustUserId": 1913,
                "adjustUserName": "黄丹1",
                "bcName": "吾在行",
                "bcCode": "0001",
                "isCompress": False,
                "fbaMainBoxCode": None,
                "shipmentTrackCode": None,
            },
            "detailFormList": [
                {
                    "reqDeployNumber": "2",
                    "useNumber": 98906,
                    "goodsCode": "ST0684",
                    "attr": None,
                    "attrId": 6,
                    "attrName": "正常",
                    "snCode": "ST0684RD0M",
                    "skuName": "红色0M",
                    "colorName": "红色",
                    "size": None,
                    "sizeName": "0M",
                    "unit": "件",
                    "weight": 183,
                    "actualStock": 0,
                    "originalCostPrice": None,
                    "presentCostPrice": None,
                    "diffMoney": None,
                    "remark": None,
                    "reqTotalMny": "54.28",
                    "totalMny": None,
                    "packingId": 10,
                    "packingName": "60*40*40",
                    "costPrice": "27.1403",
                    "categoryCode": "01",
                    "categoryId": 1,
                    "categoryName": "服装/服饰配饰",
                    "goodsId": 286821,
                    "goodsName": "服装/服饰配饰",
                    "skuCode": "0114893023189RD0M",
                    "skuId": 2880086,
                    "colorId": 17,
                    "colorCode": "RD",
                    "sizeId": 5,
                    "recid": 1
                }
            ],
            "fnSkuDataInsertForms": [
                {
                    "snCode": "ST0684RD0M",
                    "fnSku": "FNST0684RD0M",
                    "productName": "测试-产品",
                    "recid": 1
                }
            ],
            "isConfirm": False
        }
        # ②中转调拨（2种sku（ST0684RD0M、ST0683BL1L）各2件）
        data_zz_1 = {
            "mainForm": {
                "reqDeployNumber": 4,
                "billCode": info_dict['billCode'],
                "billDate": "2021-10-08T02:17:25.906Z",
                "isNeedBox": True,
                "isFixSku": True,
                "isTransferTemp": True,
                "relationshipCode": None,
                "isRelatedDeploy": False,
                "fbaWarehouseShortCode": "CS-0066",
                "receivePersonZipcode": "562762",
                "receivePersonCountryId": 178,
                "receivePersonCountry": "中国",
                "logistRequirement": 400,
                "fbaSenderAddress": "Yuhang Hangzhou Zhejiang Province",
                "fbaReceiverAddress": "马德里库里斯班144号",
                "fbaReceiverAddressId": 195,
                "applyPerson": None,
                "applyPersonId": 1913,
                "applyPersonName": "黄丹1",
                "companyId": 10,
                "bcId": 1,
                "companyName": "ZIBUYU INTERNATIONAL LIMITED",
                "companyCode": "0010",
                "deployOutWarehouseId": 26,
                "deployOutWarehouseCode": "026",
                "deployOutWarehouseName": "杭州五洲仓",
                "deployInWarehouseId": 97,
                "deployInWarehouseCode": "089",
                "deployInWarehouseName": "美欧通CA 4号中转仓",
                "status": 100,
                "creator": None,
                "reqDeployAmount": "79.47",
                "actDeployNumber": None,
                "deployBillCode": None,
                "auditor": None,
                "storeIdList": [
                    5
                ],
                "storeId": 5,
                "storeName": "WISH金鑫icen3",
                "remark": "测试数据-黄丹---中转调拨",
                "store": None,
                "mainIds": [],
                "totalWeight": 80,
                "marketId": 4,
                "marketName": "美国站",
                "marketCode": "ATVPDKIKX0DER",
                "finalWarehouse": "FBA仓",
                "adjustUserId": 1913,
                "adjustUserName": "黄丹1",
                "bcName": "吾在行",
                "bcCode": "0001",
                "isCompress": True,
                "fbaMainBoxCode": None,
                "shipmentTrackCode": None
            },
            "detailFormList": [
                {
                    "reqDeployNumber": "2",
                    "useNumber": 98904,
                    "goodsCode": "ST0684",
                    "attr": None,
                    "attrId": 6,
                    "attrName": "正常",
                    "snCode": "ST0684RD0M",
                    "skuName": "红色0M",
                    "colorName": "红色",
                    "size": None,
                    "sizeName": "0M",
                    "unit": "件",
                    "weight": 183,
                    "actualStock": 0,
                    "originalCostPrice": None,
                    "presentCostPrice": None,
                    "diffMoney": None,
                    "remark": None,
                    "reqTotalMny": "27.14",
                    "totalMny": None,
                    "packingId": 10,
                    "packingName": "60*40*40",
                    "costPrice": "27.1403",
                    "categoryCode": "01",
                    "categoryId": 1,
                    "categoryName": "服装/服饰配饰",
                    "goodsId": 286821,
                    "goodsName": "服装/服饰配饰",
                    "skuCode": "0114893023189RD0M",
                    "skuId": 2880086,
                    "colorId": 17,
                    "colorCode": "RD",
                    "sizeId": 5,
                    "recid": 1
                },
                {
                    "reqDeployNumber": "2",
                    "useNumber": 9653,
                    "goodsCode": "ST0683",
                    "attr": None,
                    "attrId": 6,
                    "attrName": "正常",
                    "snCode": "ST0683BL1L",
                    "skuName": "蓝色1L",
                    "colorName": "蓝色",
                    "size": None,
                    "sizeName": "1L",
                    "unit": "件",
                    "weight": 183,
                    "actualStock": 0,
                    "originalCostPrice": None,
                    "presentCostPrice": None,
                    "diffMoney": None,
                    "remark": None,
                    "reqTotalMny": "12.60",
                    "totalMny": None,
                    "packingId": 10,
                    "packingName": "60*40*40",
                    "costPrice": "12.6000",
                    "categoryCode": "01",
                    "categoryId": 1,
                    "categoryName": "服装/服饰配饰",
                    "goodsId": 286820,
                    "goodsName": "服装/服饰配饰",
                    "skuCode": "0114893023151BL1L",
                    "skuId": 2880048,
                    "colorId": 3,
                    "colorCode": "BL",
                    "sizeId": 7,
                    "recid": 2
                }
            ],
            "fnSkuDataInsertForms": [
                {
                    "snCode": "ST0684RD0M",
                    "fnSku": "FNST0684RD0M",
                    "productName": "测试-产品",
                    "recid": 1
                },
                {
                    "snCode": "ST0683BL1L",
                    "fnSku": "FNST0683BL1L",
                    "productName": "测试-sku-丹",
                    "recid": 2
                }
            ],
            "isConfirm": False
        }
        # ③中转调拨（1种sku（ST0684RD0M）3件）
        data_zz_2 = {
            "mainForm": {
                "reqDeployNumber": 2,
                "billCode": info_dict['billCode'],
                "billDate": "2021-11-01T02:11:36.657Z",
                "isNeedBox": True,
                "isFixSku": False,
                "isTransferTemp": True,
                "relationshipCode": None,
                "isRelatedDeploy": False,
                "fbaWarehouseShortCode": None,
                "receivePersonZipcode": None,
                "receivePersonCountryId": 178,
                "receivePersonCountry": "中国",
                "logistRequirement": 400,
                "fbaSenderAddress": "Yuhang Hangzhou Zhejiang Province",
                "fbaReceiverAddress": None,
                "fbaReceiverAddressId": None,
                "applyPerson": None,
                "applyPersonId": 1913,
                "applyPersonName": "黄丹1",
                "companyId": 10,
                "bcId": 1,
                "companyName": "ZIBUYU INTERNATIONAL LIMITED",
                "companyCode": "0010",
                "deployOutWarehouseId": 26,
                "deployOutWarehouseCode": "026",
                "deployOutWarehouseName": "杭州五洲仓",
                "deployInWarehouseId": 97,
                "deployInWarehouseCode": "089",
                "deployInWarehouseName": "美欧通CA 4号中转仓",
                "status": 100,
                "creator": None,
                "reqDeployAmount": "54.28",
                "actDeployNumber": None,
                "deployBillCode": None,
                "auditor": None,
                "storeIdList": [
                    5
                ],
                "storeId": 5,
                "storeName": "WISH金鑫icen3",
                "remark": "测试-中转调拨-非混装-单品2件-丹",
                "store": None,
                "mainIds": [],
                "totalWeight": 40,
                "marketId": 4,
                "marketName": "美国站",
                "marketCode": "ATVPDKIKX0DER",
                "finalWarehouse": "FBA仓",
                "adjustUserId": 1913,
                "adjustUserName": "黄丹1",
                "bcName": "吾在行",
                "bcCode": "0001",
                "isCompress": False,
                "fbaMainBoxCode": None,
                "shipmentTrackCode": None
            },
            "detailFormList": [
                {
                    "reqDeployNumber": "2",
                    "useNumber": 99793,
                    "goodsCode": "ST0684",
                    "attr": None,
                    "attrId": 6,
                    "attrName": "正常",
                    "snCode": "ST0684RD0M",
                    "skuName": "红色0M",
                    "colorName": "红色",
                    "size": None,
                    "sizeName": "0M",
                    "unit": "件",
                    "weight": 183,
                    "actualStock": 0,
                    "originalCostPrice": None,
                    "presentCostPrice": None,
                    "diffMoney": None,
                    "remark": None,
                    "reqTotalMny": "54.28",
                    "totalMny": None,
                    "packingId": 10,
                    "packingName": "60*40*40",
                    "costPrice": "27.1403",
                    "categoryCode": "01",
                    "categoryId": 1,
                    "categoryName": "服装/服饰配饰",
                    "goodsId": 286821,
                    "goodsName": "服装/服饰配饰",
                    "skuCode": "0114893023189RD0M",
                    "skuId": 2880086,
                    "colorId": 17,
                    "colorCode": "RD",
                    "sizeId": 5,
                    "recid": 1
                }
            ],
            "fnSkuDataInsertForms": [
                {
                    "snCode": "ST0684RD0M",
                    "fnSku": "FNST0684RD0M",
                    "productName": "测试-产品",
                    "recid": 1
                }
            ],
            "isConfirm": False
        }
    elif info_dict['conf'] == 'test':
        # ①FBA调拨（1种sku（ST0684RD0M）2件）
        data_fba = {
            "mainForm": {
                "reqDeployNumber": 2,
                "billCode": info_dict['billCode'],
                "billDate": "2021-10-12T07:41:33.286Z",
                "isNeedBox": True,
                "isFixSku": None,
                "isTransferTemp": False,
                "relationshipCode": None,
                "isRelatedDeploy": False,
                "fbaWarehouseShortCode": "666",
                "receivePersonZipcode": "310001",
                "receivePersonCountryId": 178,
                "receivePersonCountry": "中国",
                "logistRequirement": 400,
                "fbaSenderAddress": "Yuhang Hangzhou Zhejiang Province",
                "fbaReceiverAddress": "4号",
                "fbaReceiverAddressId": 179,
                "applyPerson": None,
                "applyPersonId": 3159,
                "applyPersonName": "黄丹1",
                "companyId": 10,
                "bcId": 1,
                "companyName": "ZIBUYU INTERNATIONAL LIMITED",
                "companyCode": "0010",
                "deployOutWarehouseId": 26,
                "deployOutWarehouseCode": "026",
                "deployOutWarehouseName": "杭州五洲仓",
                "deployInWarehouseId": 11,
                "deployInWarehouseCode": "011",
                "deployInWarehouseName": "FBA仓",
                "status": 100,
                "creator": None,
                "reqDeployAmount": "52.41",
                "actDeployNumber": None,
                "deployBillCode": None,
                "auditor": None,
                "storeIdList": [
                    5
                ],
                "storeId": 5,
                "storeName": "WISH金鑫icen3",
                "remark": "测试数据-test-FBA调拨",
                "store": None,
                "mainIds": [],
                "totalWeight": 40,
                "marketId": 4,
                "marketName": "美国站",
                "marketCode": "ATVPDKIKX0DER",
                "finalWarehouse": None,
                "adjustUserId": 3159,
                "adjustUserName": "黄丹1",
                "bcName": "吾在行",
                "bcCode": "0001",
                "isCompress": False,
                "fbaMainBoxCode": None,
                "shipmentTrackCode": None
            },
            "detailFormList": [
                {
                    "reqDeployNumber": "2",
                    "useNumber": 971,
                    "goodsCode": "ST0684",
                    "attr": None,
                    "attrId": 6,
                    "attrName": "正常",
                    "snCode": "ST0684RD0M",
                    "skuName": "红色0M",
                    "colorName": "红色",
                    "size": None,
                    "sizeName": "0M",
                    "unit": "件",
                    "weight": 183,
                    "actualStock": 0,
                    "originalCostPrice": None,
                    "presentCostPrice": None,
                    "diffMoney": None,
                    "remark": None,
                    "reqTotalMny": "52.41",
                    "totalMny": None,
                    "packingId": 10,
                    "packingName": "60*40*40",
                    "costPrice": "26.2069",
                    "categoryCode": "01",
                    "categoryId": 1,
                    "categoryName": "服装/服饰配饰",
                    "goodsId": 286821,
                    "goodsName": "服装/服饰配饰",
                    "skuCode": "0114893023189RD0M",
                    "skuId": 2880086,
                    "colorId": 17,
                    "colorCode": "RD",
                    "sizeId": 5,
                    "recid": 2,
                    "goodsBcName": None,
                    "goodsBcId": None,
                    "goodsBcCode": None
                }
            ],
            "fnSkuDataInsertForms": [
                {
                    "snCode": "ST0684RD0M",
                    "fnSku": "FNST0684RD0M",
                    "productName": "测试sku",
                    "recid": 1
                }
            ],
            "isConfirm": False
        }
        # ②中转调拨（2种sku（ST0684RD0M、ST0683BL1L）各2件，isFixSku-false-非混装）
        data_zz_1 = {
            "mainForm": {
                "reqDeployNumber": 4,
                "billCode": info_dict['billCode'],
                "billDate": "2021-10-12T07:55:46.917Z",
                "isNeedBox": True,
                "isFixSku": False,
                "isTransferTemp": True,
                "relationshipCode": None,
                "isRelatedDeploy": False,
                "fbaWarehouseShortCode": None,
                "receivePersonZipcode": None,
                "receivePersonCountryId": 178,
                "receivePersonCountry": "中国",
                "logistRequirement": 400,
                "fbaSenderAddress": "Yuhang Hangzhou Zhejiang Province",
                "fbaReceiverAddress": None,
                "fbaReceiverAddressId": None,
                "applyPerson": None,
                "applyPersonId": 3159,
                "applyPersonName": "黄丹1",
                "companyId": 10,
                "bcId": 1,
                "companyName": "ZIBUYU INTERNATIONAL LIMITED",
                "companyCode": "0010",
                "deployOutWarehouseId": 26,
                "deployOutWarehouseCode": "026",
                "deployOutWarehouseName": "杭州五洲仓",
                "deployInWarehouseId": 97,
                "deployInWarehouseCode": "089",
                "deployInWarehouseName": "美欧通CA 4号中转仓",
                "status": 100,
                "creator": None,
                "reqDeployAmount": "38.81",
                "actDeployNumber": None,
                "deployBillCode": None,
                "auditor": None,
                "storeIdList": [
                    5
                ],
                "storeId": 5,
                "storeName": "WISH金鑫icen3",
                "remark": "测试数据-test-中转调拨",
                "store": None,
                "mainIds": [],
                "totalWeight": 20.142,
                "marketId": 4,
                "marketName": "美国站",
                "marketCode": "ATVPDKIKX0DER",
                "finalWarehouse": "FBA仓",
                "adjustUserId": 3159,
                "adjustUserName": "黄丹1",
                "bcName": "吾在行",
                "bcCode": "0001",
                "isCompress": False,
                "fbaMainBoxCode": None,
                "shipmentTrackCode": None
            },
            "detailFormList": [
                {
                    "reqDeployNumber": "2",
                    "useNumber": 971,
                    "goodsCode": "ST0684",
                    "attr": None,
                    "attrId": 6,
                    "attrName": "正常",
                    "snCode": "ST0684RD0M",
                    "skuName": "红色0M",
                    "colorName": "红色",
                    "size": None,
                    "sizeName": "0M",
                    "unit": "件",
                    "weight": 183,
                    "actualStock": 0,
                    "originalCostPrice": None,
                    "presentCostPrice": None,
                    "diffMoney": None,
                    "remark": None,
                    "reqTotalMny": "26.21",
                    "totalMny": None,
                    "packingId": 10,
                    "packingName": "60*40*40",
                    "costPrice": "26.2069",
                    "categoryCode": "01",
                    "categoryId": 1,
                    "categoryName": "服装/服饰配饰",
                    "goodsId": 286821,
                    "goodsName": "服装/服饰配饰",
                    "skuCode": "0114893023189RD0M",
                    "skuId": 2880086,
                    "colorId": 17,
                    "colorCode": "RD",
                    "sizeId": 5,
                    "recid": 1
                },
                {
                    "reqDeployNumber": "2",
                    "useNumber": 10000,
                    "goodsCode": "ST0683",
                    "attr": None,
                    "attrId": 6,
                    "attrName": "正常",
                    "snCode": "ST0683BL1L",
                    "skuName": "蓝色1L",
                    "colorName": "蓝色",
                    "size": None,
                    "sizeName": "1L",
                    "unit": "件",
                    "weight": 142,
                    "actualStock": 0,
                    "originalCostPrice": None,
                    "presentCostPrice": None,
                    "diffMoney": None,
                    "remark": None,
                    "reqTotalMny": "12.60",
                    "totalMny": None,
                    "packingId": 10,
                    "packingName": "60*40*40",
                    "costPrice": "12.6000",
                    "categoryCode": "01",
                    "categoryId": 1,
                    "categoryName": "服装/服饰配饰",
                    "goodsId": 286820,
                    "goodsName": "服装/服饰配饰",
                    "skuCode": "0114893023151BL1L",
                    "skuId": 2880048,
                    "colorId": 3,
                    "colorCode": "BL",
                    "sizeId": 7,
                    "recid": 2
                }
            ],
            "fnSkuDataInsertForms": [
                {
                    "snCode": "ST0684RD0M",
                    "fnSku": "FNST0684RD0M",
                    "productName": "测试sku",
                    "recid": 1
                },
                {
                    "snCode": "ST0683BL1L",
                    "fnSku": "FNST0683BL1L",
                    "productName": "测试-sku-丹",
                    "recid": 2
                }
            ],
            "isConfirm": False
        }
        # ③中转调拨（1种sku（ST0684RD0M）3件）
        data_zz_2 = {
            "mainForm": {
                "reqDeployNumber": 3,
                "billCode": info_dict['billCode'],
                "billDate": "2021-11-01T02:31:34.774Z",
                "isNeedBox": True,
                "isFixSku": False,
                "isTransferTemp": True,
                "relationshipCode": None,
                "isRelatedDeploy": False,
                "fbaWarehouseShortCode": None,
                "receivePersonZipcode": None,
                "receivePersonCountryId": 178,
                "receivePersonCountry": "中国",
                "logistRequirement": 400,
                "fbaSenderAddress": "Yuhang Hangzhou Zhejiang Province",
                "fbaReceiverAddress": None,
                "fbaReceiverAddressId": None,
                "applyPerson": None,
                "applyPersonId": 3159,
                "applyPersonName": "黄丹1",
                "companyId": 10,
                "bcId": 1,
                "companyName": "ZIBUYU INTERNATIONAL LIMITED",
                "companyCode": "0010",
                "deployOutWarehouseId": 26,
                "deployOutWarehouseCode": "026",
                "deployOutWarehouseName": "杭州五洲仓",
                "deployInWarehouseId": 97,
                "deployInWarehouseCode": "089",
                "deployInWarehouseName": "美欧通CA 4号中转仓",
                "status": 100,
                "creator": None,
                "reqDeployAmount": "52.41",
                "actDeployNumber": None,
                "deployBillCode": None,
                "auditor": None,
                "storeIdList": [
                    5
                ],
                "storeId": 5,
                "storeName": "WISH金鑫icen3",
                "remark": "测试-中转调拨-非混装-单品2件-丹",
                "store": None,
                "mainIds": [],
                "totalWeight": 40,
                "marketId": 4,
                "marketName": "美国站",
                "marketCode": "ATVPDKIKX0DER",
                "finalWarehouse": "FBA仓",
                "adjustUserId": 3159,
                "adjustUserName": "黄丹1",
                "bcName": "吾在行",
                "bcCode": "0001",
                "isCompress": False,
                "fbaMainBoxCode": None,
                "shipmentTrackCode": None
            },
            "detailFormList": [
                {
                    "reqDeployNumber": "3",
                    "useNumber": 931,
                    "goodsCode": "ST0684",
                    "attr": None,
                    "attrId": 6,
                    "attrName": "正常",
                    "snCode": "ST0684RD0M",
                    "skuName": "红色0M",
                    "colorName": "红色",
                    "size": None,
                    "sizeName": "0M",
                    "unit": "件",
                    "weight": 183,
                    "actualStock": 0,
                    "originalCostPrice": None,
                    "presentCostPrice": None,
                    "diffMoney": None,
                    "remark": None,
                    "reqTotalMny": "52.41",
                    "totalMny": None,
                    "packingId": 10,
                    "packingName": "60*40*40",
                    "costPrice": "26.2069",
                    "categoryCode": "01",
                    "categoryId": 1,
                    "categoryName": "服装/服饰配饰",
                    "goodsId": 286821,
                    "goodsName": "服装/服饰配饰",
                    "skuCode": "0114893023189RD0M",
                    "skuId": 2880086,
                    "colorId": 17,
                    "colorCode": "RD",
                    "sizeId": 5,
                    "recid": 1
                }
            ],
            "fnSkuDataInsertForms": [
                {
                    "snCode": "ST0684RD0M",
                    "fnSku": "FNST0684RD0M",
                    "productName": "测试sku",
                    "recid": 1
                }
            ],
            "isConfirm": False
        }
    else:
        raise Exception('传入的参数：conf_url 有误！')
    # 3）请求接口，生成FBA调拨申请单，获取申请单mainId
    logger.info('开始请求新增接口！')
    res = requests.post(url=url, json=data_fba, headers=info_dict['base_headers'])
    # 4）接口返回数据处理
    tag = res.json()
    if tag['status'] == -1:
        logger.error('新增FBA调拨申请单失败，接口有误！！！')
    else:
        main_id = tag['data']['mainId']
        logger.info('新增FBA调拨申请单成功！')
        info_dict['mainId'] = main_id
        return info_dict


# 4.审核调拨申请单
def test_04():
    # 1)拼接接口url
    main_id = info_dict['mainId']
    url = info_dict['conf_url'] + f'stockdata/v1/stockDeployRequest/audit/{main_id}'
    # 2)请求接口，审核
    res=requests.post(url=url, headers=info_dict['base_headers'])
    tag=res.json()
    if tag['status'] == 0:
        logger.info('调拨申请单审核成功！')
    else:
        logger.error('调拨申请单审核失败！')
        logger.error(tag['msg'])





# 5.1释放redis锁
def test_05_redis():
    # 1)拼接接口url
    processkey = info_dict['processKey']
    url = info_dict['conf_url'] + f'bfferp/batch/v1/queryProcess?processKey={processkey}'
    # 2）请求接口
    res = requests.post(url=url, headers=info_dict['base_headers'])
    if res.json()['data']['isAsyncEnd']:
        # 任务完毕，则删除锁
        url1 = info_dict['conf_url'] + f'bfferp/batch/v1/delProcess?processKey={processkey}'
        requests.post(url=url1, headers=info_dict['base_headers'])
        logger.info('删除redis锁成功！')
    else:
        # 任务未完成，继续查询任务情况
        time.sleep(1)
        test_05_redis()


# 5.2生成调拨订单
def test_05():
    # 1)拼接接口url
    url = info_dict['conf_url'] + 'stockdata/v1/stockDeployRequest/generateDeployOrder'
    # 2）参数准备
    data = []
    data.append(int(info_dict['mainId']))
    # 3）请求接口
    res = requests.post(url=url, json=data, headers=info_dict['base_headers'])
    # 4）接口返回数据处理
    status = res.json()['status']
    processkey = res.json()['data']
    info_dict['status'] = status
    info_dict['processKey'] = processkey
    if status == 0:
        logger.info('成功生成调拨订单')
        # 调用接口，释放redis锁
        test_05_redis()
    else:
        logger.error('生成调拨订单---失败！')


# 6.根据调拨申请单号，查询对应调拨单信息
def test_06():
    # 1)拼接接口url
    url = info_dict['conf_url'] + 'stockdata/v1/stockDeployRequest/list/mainBill?pageNo=1&pageSize=1000'
    # 2）参数准备
    data = {
        "billCode": info_dict['billCode'],
        "applyPersonId": None,
        "billDateEnd": None,
        "billDateStart": None,
        "companyId": None,
        "creator": None,
        "deployBillCode": None,
        "deployOutWarehouseId": None,
        "goodsCode": None,
        "snCode": None,
        "status": None,
        "storeIdList": [],
        "mainIds": [],
        "isGenerateDeployBill": None,
        "attrIdList": [],
        "receivePersonCountryId": None,
        "logistRequirement": None,
        "fbaWarehouseShortCode": None,
        "isTransferTemp": None,
        "isFixSku": None,
        "isNeedBox": None,
        "isCompress": None
    }
    # 3）请求接口
    res = requests.post(url=url, json=data, headers=info_dict['base_headers'])
    # 4）接口返回数据处理
    deploybillcode = res.json()['data'][0]['deployBillCode']
    deploybillid = res.json()['data'][0]['deployBillId']
    info_dict['deployBillCode'] = deploybillcode
    info_dict['deployBillId'] = deploybillid
    return info_dict


# 7.调拨订单审核
def test_07():
    # 1)拼接接口url
    url = info_dict['conf_url'] + 'stockdata/v1/stockdeploy/auditStockDeploy'
    # 2）参数准备
    data = []
    data.append(int(info_dict['deployBillId']))
    # 3）请求接口
    requests.post(url=url, json=data, headers=info_dict['base_headers'])
    logger.info('订单已审核！')


# 8.调拨订单转仓
def test_08():
    # 1)拼接接口url
    url = info_dict['conf_url'] + 'stockdata/v1/stockdeploy/transferStockDeploy'
    # 2）参数准备
    data = []
    data.append(int(info_dict['deployBillId']))
    # 3）请求接口
    requests.post(url=url, json=data, headers=info_dict['base_headers'])
    logger.info('订单已转仓！')


# 9.打印拣货单

def test_09():
    # 1)，根据调拨订单号查询该单据id
    # <1>拼接接口url
    url_01 = info_dict['conf_url'] + 'wmsdata/v1/stockOutRequest/list?pageNo=1&pageSize=1000&total=1&offset=0'
    # <2>参数准备
    data_01 = {
        "sourceBillCode": info_dict['deployBillCode'],
        "isCompress": None,
        "isDeployBack": None,
        "suggestedBoxCode": None,
        "deployBillType": None,
        "isEurope": None,
        "deployMoveType": None,
        "billStatusList": [
            100,
            200,
            300,
            400,
            450,
            500,
            520,
            600,
            700,
            1000
        ],
        "billStatusListTip": [],
        "companyId": None,
        "billCode": None,
        "warehouseId": None,
        "startBillDate": None,
        "endBillDate": None,
        "billStatus": None,
        "goodsCode": None,
        "snCode": None,
        "deliveryBillCode": None,
        "pickingBillCode": None,
        "applyManName": None,
        "warehouseName": None,
        "isPrintTrackNum": None,
        "isPrintLogisticsSheet": None,
        "fnSku": None,
        "trackNumber": None,
        "fbaOrderId": None,
        "targetWarehouseId": None,
        "logistCompanyIdList": [],
        "logistWayIdList": [],
        "billType": 500,
        "isSecondCheck": None,
        "relationshipCode": None,
        "fbaBoxCode": None,
        "isTransferTemp": None,
        "isFixSku": None,
        "isNeedBox": None,
        "idList": [],
        "mainIds": []
    }
    # <3>数据处理-获取id
    res_01 = requests.post(url=url_01, json=data_01, headers=info_dict['base_headers'])
    bill_id = res_01.json()['data'][0]['id']
    info_dict['SOR_code']=res_01.json()['data'][0]['billCode']
    info_dict['id'] = bill_id
    # 2)根据id，打印拣货单
    # <1>拼接接口url
    url_02 = info_dict['conf_url'] + 'wmsdata/v1/stockOutRequestPick/generateFBAPickingBill'
    # <2>参数准备
    l = []
    l.append(int(info_dict['id']))
    data_02 = {}
    data_02['ids'] = l
    # print('打印拣货单的入参：{}'.format(data_02))
    # <3>数据处理-获取拣货单号
    res_02 = requests.post(url=url_02, json=data_02, headers=info_dict['base_headers'])
    jhd = res_02.json()['data']['pickingTaskBillVoList'][0]['pickingTaskMainVo']['billCode']
    logger.info('打印拣货单完毕！')
    info_dict['JHD'] = jhd
    return info_dict


# 10.拣货完成

def test_10():
    # 1)根据拣货单号，更改拣货方式pda,并查询出拣货单id
    def update_is_use_pda():
        sql_01 = f"""
            UPDATE zby_wmsdata.wms_picking_bill_main 
            SET is_use_pda = 0
            WHERE picking_code='{info_dict['JHD']}'
           """
        sql_02 = f"""
            select id 
            from  zby_wmsdata.wms_picking_bill_main
            WHERE picking_code='{info_dict['JHD']}'
"""
        # 生成对应环境的数据库对象
        my_db = DB(info_dict['conf'])
        logger.info(f'执行如下sql>>{sql_01}')
        my_db.execute_sql(sql_01)
        # 查询出拣货单id
        logger.info(f'执行如下sql>>{sql_02}')
        res = my_db.execute_sql(sql_02)
        pick_id = res[0][0]
        l = []
        l.append(pick_id)
        info_dict['pick_id'] = l
        return info_dict

    # #2)调用拣货完成接口
    def pick_complete():
        # 1)拼接接口url
        url = info_dict['conf_url'] + 'wmsdata/v1/pickingBill/completePickingBill'
        # 2）入参准备
        data = info_dict['pick_id']
        # 3）请求接口，执行拣货完成操作
        res = requests.post(url=url, headers=info_dict['base_headers'], json=data)
        # 3）接口返回数据处理
        tag = res.json()
        if tag['status'] == 0:
            logger.info(f'拣货成功，{tag["msg"]}')
        else:
            logger.error(f'拣货失败，{tag["msg"]}')


    update_is_use_pda()
    pick_complete()
    logger.info('拣货完成！')
    return info_dict

#11.FBA/中转复核扫码
def test_11():
    for i in range(2):
        #执行两次
        # 1.申请码
        url_01 = info_dict['conf_url'] + 'wmsdata/v1/stockOutRequestSplitBox/applySuggestedBox'
        data_01 = {'mainBillCode': info_dict['SOR_code']}
        res1 = requests.post(url=url_01, params=data_01, headers=info_dict['base_headers'])
        tag1 = res1.json()
        if tag1['status'] == 0:
            info_dict['SuggestedBoxCode'] = tag1['data']
            logger.info(info_dict['SuggestedBoxCode'])
        else:
            logger.error('申请系统分箱码失败！')
            logger.error( tag1['msg'])


        # 2.扫描系统分箱码
        url_02 = info_dict['conf_url'] + 'wmsdata/v1/stockOutRequestSplitBox/printForSysBox'
        data_02 = {'mainBillCode': info_dict['SOR_code'], 'sysBoxCode': info_dict['SuggestedBoxCode']}
        res2 = requests.post(url=url_02, params=data_02, headers=info_dict['base_headers'])
        tag2 = res2.json()
        if tag2['status'] == 0:
            pass
        else:
            logger.error('扫描系统分箱码失败！')
            logger.error(tag2['msg'])

        # 3.回车sku
        url_03 = info_dict['conf_url'] + 'wmsdata/v1/stockOutRequestCheck/scanAndCheckBySkuForFba'
        data_03 = {"stockoutBillMainCode": info_dict['SOR_code'],
                   "pickingCode": info_dict['JHD'],
                   "suggestedBoxCode": info_dict['SuggestedBoxCode'],
                   "snCode": "ST0684RD0M",
                   "purchaseBatchCode": "0000",
                   "weight": None,
                   "allweight": None,
                   "isConfirm": True}
        res3 = requests.post(url=url_03, json=data_03, headers=info_dict['base_headers'])
        tag3 = res3.json()
        if tag3['status'] == 0:
            pass
        else:
            logger.error('扫描sku失败！')
            logger.error( tag3['msg'])

        # 4.填写箱子重量
        url_04 = info_dict['conf_url'] + 'wmsdata/v1/stockOutRequestSplitBox/updateBoxRecord'
        data_04 = [{"sysBoxCode":info_dict['SuggestedBoxCode'],"weight":i,"billCode":info_dict['SOR_code']}]
        res4 = requests.post(url=url_04, json=data_04, headers=info_dict['base_headers'])
        tag4 = res4.json()
        if tag4['status'] == 0:
            pass
        else:
            logger.error('填写箱子重量失败！')
            logger.error( tag4['msg'])
    logger.info('复核扫码完成！')

#12.点击扫码完成
def test_12():
    url = info_dict['conf_url'] + 'wmsdata/v1/stockOutRequestCheck/scanCheckComplete?haveConfirm=false'
    data = [info_dict['id']]
    res1 = requests.post(url=url, json=data, headers=info_dict['base_headers'])
    tag1 = res1.json()
    if tag1['status'] == 0:
        logger.info('点击扫码完成成功！')
    else:
        logger.error('点击扫码完成失败！')
        logger.error(tag1['msg'])


#13.点击装箱完成
def test_13():
    url = info_dict['conf_url'] + 'wmsdata/v1/stockOutRequestCheck/packageComplete?haveConfirm=true'
    data = [info_dict['id']]
    res1 = requests.post(url=url, json=data, headers=info_dict['base_headers'])
    tag1 = res1.json()
    if tag1['status'] == 0:
        logger.info('点击装箱完成成功')
    else:
        logger.error('点击装箱完成失败！')
        logger.error(tag1['msg'])

# 生成FBA调拨单主函数
def main_deploy(conf):
    # 1.登录指定环境，获取接口关联字典
    global info_dict
    info_dict = login(conf)
    # 2.生成单据编号
    logger.info('<<<———调拨开始！———>>>')
    logger.info('<<<————开始生成单据编号————>>>')
    test_02()
    # 3.新增FBA调拨申请单
    logger.info('<<<————新增FBA调拨申请单————>>>')
    test_03()
    time.sleep(1)
    # 4.审核调拨申请单
    logger.info('<<<————审核调拨申请单————>>>')
    test_04()
    # 5.生成调拨订单
    logger.info('<<<————生成调拨订单————>>>')
    test_05()
    time.sleep(1)
    # 6.查询调拨单信息
    logger.info('<<<————查询调拨单信息————>>>')
    test_06()
    # 7.调拨订单审核
    logger.info('<<<————调拨订单审核————>>>')
    test_07()
    # # 8.调拨订单转仓
    time.sleep(1)
    logger.info('<<<————调拨订单转仓————>>>')
    test_08()
    # 9.打印拣货单
    logger.info('<<<————打印拣货单————>>>')
    test_09()
    # 10.拣货完成
    logger.info('<<<————拣货完成————>>>')
    test_10()
    #11.FBA/中转复核扫码
    logger.info('<<<————开始FBA/中转复核扫码————>>>')
    test_11()
    #12.点击扫码完成
    logger.info('<<<————点击扫码完成————>>>')
    test_12()
    #13.点击装箱完成
    logger.info('<<<————点击装箱完成————>>>')
    test_13()

    # 14.展示本次调拨相关信息
    info_1=info_dict['deployBillCode']
    info_2=info_dict['SOR_code']
    logger.info('<<<————调拨结束！————>>>')
    logger.info(f'本地调拨相关信息: 调拨订单号：{info_1}，调拨申请单号：{info_2}')



# 调用主程序
if __name__ == '__main__':
    # 1）调拨主程序
    # main_deploy('dev')
    main_deploy('test')
