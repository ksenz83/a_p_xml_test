from lxml import etree as ET
from lxml import objectify
from datetime import datetime
import dateutil.parser


def get_data_from_xml(xml):
    # root = ET.fromstring(xml)
    root = objectify.fromstring(xml)
    for elem in root.getiterator():
        elem.tag = ET.QName(elem).localname
    dic = {
        'xml_type': root.tag,
        'purchase_number': root.data.purchaseNumber.text,
        'doc_publish_date_str': root.data.docPublishDate.text,
        'doc_publish_date': dateutil.parser.parse(root.data.docPublishDate.text),
        'purchase_object_info': root.data.purchaseObjectInfo.text,
        'reg_num': root.data.purchaseResponsible.responsibleOrg.regNum.text,
        'full_name': root.data.purchaseResponsible.responsibleOrg.fullName.text,
        'max_price': root.data.lot.maxPrice,
    }
    print(dic)
    return dic


if __name__ == '__main__':
    with open('test.xml', 'rb') as fobj:
        xml = fobj.read()

    get_data_from_xml(xml)