# template = { "io_tag_no": "string", "signal_name": "string", "io_type": "string", "card_type": "string", "master_card": [ {"mc_no": "number"}, {"ch_no1": "number"} ], "io_card_location": [ {"cf_no": "number"}, {"iou_no": "number"}, {"sl_no": "number"}, {"ch_no": "number"} ], "output_setting": "string" }
template = {
    "io_tag_no": "string",
    "signal_name": "string",
    "io_type": "string",
    "card_type": "string",
    "config": "nubmer",
    "master_card": {
        "mc_no": "number",
        "ch_no1": "number",
        "ch_no2": "number"
        },
    "io_card_location": {
        "cf1_no": "number",
        "cf2_no": "number",
        "iou_no": "number",
        "sl_no": "number",
        "ch_no": "number"
        },
    "fail_mode": "string"
}

flattendKeys = []
def flatten(dic, parent=""):
    """
        flatten keys of template
        and return a list of keys.
    """
    for key in dic.keys():
        if type(dic[key]) == type({}):
            flatten(dic[key], parent=key)
        else:
            if parent == "":
                flattendKeys.append(key)
            else:
                flattendKeys.append(parent + "." + key)
# def flatten(dic, parent=""):
#     for key in dic.keys():
#         if type(dic[key]) == type([]):
#             for subDic in dic[key]:
#                 flatten(subDic, parent=list(subDic.keys())[0])
#         else:
#             if parent == "":
#                 flattendKeys.append(key)
#             else:
#                 flattendKeys.append(parent + "." + key)

flatten(template)
print(flattendKeys)
