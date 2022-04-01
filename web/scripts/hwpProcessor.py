import olefile
import struct

def get_hwp_text(f):

    f = olefile.OleFileIO('/home/ec2-user/web/scripts/nari.hwp')
    dirs = f.listdir()
    header = f.openstream("FileHeader")
    header_data = header.read()
    nums = []
    for d in dirs:
        if d[0] == "BodyText":
            nums.append(int(d[1][len("Section"):]))
    sections = ["BodyText/Section" + str(x) for x in sorted(nums)]

    # 전체 text 추출
    text = ""
    for section in sections:
        bodytext = f.openstream(section)
        data = bodytext.read()

        # 각 Section 내 text 추출
        section_text = ""
        i = 0
        size = len(data)
        while i < size:
            header = struct.unpack_from("<I", data, i)[0]
            rec_type = header & 0x3ff
            rec_len = (header >> 20) & 0xfff

            if rec_type in [67]:
                rec_data = data[i + 4:i + 4 + rec_len]
                section_text += rec_data.decode('utf-16')
                section_text += "\n"

            i += 4 + rec_len
        text += section_text
        text += "\n"
    return text
