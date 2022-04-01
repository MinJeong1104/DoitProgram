import olefile
import struct

def get_hwp_text(f):

    f = olefile.OleFileIO('/home/ec2-user/web/scripts/nari.hwp')
    dirs = f.listdir()
    # HWP 파일 검증
    if ["FileHeader"] not in dirs or \
            ["\x05HwpSummaryInformation"] not in dirs:
        raise Exception("Not Valid HWP.")
    else:
        print("Valid HWP")


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
        print(data)


        # 각 Section 내 text 추출
        section_text = ""
        i = 0
        size = len(data)
        while i < size:
            header = struct.unpack_from("<I", data, i)[0]
            print("header"+str(header))
            rec_type = header & 0x3ff
            print("rec_tpye"+str(rec_type))
            rec_len = (header >> 20) & 0xfff
            print("rec_len"+str(rec_len))
            rec_data = data[i + 4:i + 4 + rec_len]
            print("rec_data"+str(rec_data))
            section_text += rec_data.decode('UTF-16', errors='ignore')
            section_text += "\n"
            print("section_text"+str(section_text))
            i += 4 + rec_len
        text += section_text
        text += "\n"
    return text
