import base64
import zlib
data = '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'

json_str = zlib.decompress(base64.b64decode(data)).decode('utf-8')
print(json_str)