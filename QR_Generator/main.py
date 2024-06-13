import qrcode


data = pandas.read_csv('name_links.csv')
data = data.to_dict()
NAME = data['Name']
LINKS = data['Links']


for index in range(0, len(NAME)):
    qr = qrcode.QRCode(
        version=11,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=5,
    )
    qr.add_data(LINKS[index])
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(f'{NAME[index]}.png')
    print(f"{NAME[index]} Complete")

