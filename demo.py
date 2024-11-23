import yaml

with open("regex.yaml", encoding="utf-8") as f:  # demo.yaml内容同上例yaml字符串
    reDict = yaml.safe_load(f)

print(reDict)
