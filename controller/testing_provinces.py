import json


def open_json(filepath):
    with open(filepath) as f:
        data = json.load(f)
    return data

def counting_districts(data):
    total_districts = ['TAPLEJUNG', 'SANKHUWASABHA', 'SOLUKHUMBU', 'PANCHTHAR', 'ILLAM', 'TERHATHUM', 
                       'DHANKUTA', 'BHOJPUR', 'KHOTANG', 'OKHALDHUNGA', 'UDAYAPUR', 'JHAPA', 'MORANG', 
                       'SUNSARI', 'SAPTARI', 'SIRAHA', 'DHANUSHA', 'MAHOTTARI', 'SARLAHI', 'RAUTAHAT', 
                       'BARA', 'PARSA', 'DOLAKHA', 'SINDHUPALCHOK', 'RASUWA', 'RAMECHAP', 'SINDHULI', 
                       'KAVRE', 'BHAKTAPUR', 'LALITPUR', 'KATHMANDU', 'NUWAKOT', 'DHADING', 'MAKAWANPUR', 
                       'CHITWAN', 'MANANG', 'MUSTANG', 'GORKHA', 'LAMJUNG', 'TANAHU', 'KASKI', 'PARBAT', 
                       'SYANGJA', 'MYAGDI', 'BAGLUNG', 'NAWALPARASI EAST', 'PALPA', 'GULMI', 'ARGHAKHANCHI', 
                       'NAWALPARASI WEST', 'RUPANDEHI', 'KAPILBASTU', 'DANG', 'BANKE', 'BARDIYA', 'RUKUM EAST', 
                       'PYUTHAN', 'ROLPA', 'DOLPA', 'MUGU', 'HUMLA', 'JUMLA', 'KALIKOT', 'RUKUM WEST', 'SALYAN', 
                       'JAJARKOT', 'DAILEKH', 'SURKHET', 'BAJURA', 'BAJHANG', 'DARCHULA', 'ACHHAM', 'DOTI', 
                       'BAITADI', 'DADELDHURA', 'KAILALI', 'KANCHANPUR']
    districts = []
    counter = 0
    for a in data:
        for key, value in a.items():
            if key == 'District':
                counter += 1
                districts.append(value)

    not_present = []
    for i in total_districts:
        if i not in districts:
            not_present.append(i)
        else:
            continue

    duplicate = []
    unique = []
    duplicate_counter = 0
    for a in districts:
        if a not in unique:
            unique.append(a)
        else:
            duplicate_counter += 1
            duplicate.append(a)


    left = len(total_districts)-counter

    print(f" The total number of district: {counter} i.e remaining - {left}.  \n District not present are {not_present} \n duplicate_count: {duplicate_counter}, \n {duplicate}")
    return counter

if __name__ == "__main__":
    a = open_json('raw_data/2079_data/buckwheat_yield.json')
    b = open_json('raw_data/2079_data/barley_yield.json')
    c = open_json('raw_data/2079_data/millet_yield.json')
    d = open_json('raw_data/2079_data/maize_yield.json')
    e = open_json('raw_data/2079_data/wheat_yield.json')
    f = open_json('raw_data/2079_data/paddy_yield.json')
    g = open_json('raw_data/2078_data/2078_paddy_yield.json')

    counting_districts(a)
    counting_districts(b)
    counting_districts(c)
    counting_districts(d)
    counting_districts(e)
    counting_districts(f)
    counting_districts(g)

