from monkeylearn import MonkeyLearn

ml = MonkeyLearn('0fc89d43abdd327d2a1913034935b4470ce2391f')
# data = ["Exponent Box, print-in-place support-free box with logarithmic gearing! Model and print by on and patreon! Printed in Peak Green PLA+ on Mini"]
data = ["This cyber rob is really cute, I necessarily had to print it. Have you already printed it? • Cyber rob File from @cults3d Designer by @af_inventions & @cyber_3dprinter Maker @madeofrancesco Filament by @cyber_filament • Extruder and hotend @microswissllc Remote control @octoprint3d on @raspberrypifoundation by @meloperoelectronics Multicolor platform @mosaicmfg Nozzle @zodiacnozzle • Take a look at the link in bio •"]
model_id = 'ex_YCya9nrn'
result = ml.extractors.extract(model_id, data)

print(type(result.body[0]))
# print(result.body[0]["extractions"])
# print(result.body[0]["extractions"][6]["parsed_value"])

# relevanceList = []
# for item in result.body[0]["extractions"]:
#     print(item["parsed_value"] + "|" + item["relevance"])

# relevanceList.sort(reverse=True)
# print(*relevanceList, sep = "\n")

# from monkeylearn import MonkeyLearn
#
# ml = MonkeyLearn('0fc89d43abdd327d2a1913034935b4470ce2391f')
# data = ["Elon Musk has shared a photo of the spacesuit designed by SpaceX. This is the second image shared of the new design and the first to feature the spacesuit’s full-body look."]
# model_id = 'ex_YCya9nrn'
# result = ml.extractors.extract(model_id, data)
#
# # print(result.body[0]["extractions"][6]["parsed_value"])
# for item in result.body[0]["extractions"]:
#     print(item["parsed_value"])