import requests
from bs4 import BeautifulSoup

run = True
directory = r'./arquivos'

#lista a ser baixada
jogadores = [
'Neymar Brasil Figurinha',
'Lionel Messi  Argentina Figurinha',
'Enner Valencia  Equador Figurinha',
'Luis Suárez  Uruguai Figurinha',
'Dušan Vlahović  Sérvia Figurinha',
'Granit Xhaka  Suíça Figurinha',
'Pedri   Espanha Figurinha',
'Kylian Mbappé  França Figurinha',
'Kevin De Bruyne Bélgica Figurinha',
'Eriksen   Dinamarca Figurinha',
'Virgil Van Dijk Holanda Figurinha',
'Modric   Croácia Figurinha',
'Harry Kane  Inglaterra Figurinha',
'Thomas Müller  Alemanha Figurinha',
'Cristiano Ronaldo  Portugal Figurinha',
'Robert Lewandowski  Polônia Figurinha',
'Gareth Bale  País de Gales Figurinha',
'Almoez Ali  Catar Figurinha',
'Sardar Azmoun  Irã Figurinha',
'Heung-min Son  Coreia do Sul Figurinha',
'Minamino   Japão Figurinha',
'Abdulrahman Ghareeb  Arábia Saudita Figurinha',
'Aaron Mooy  Austrália Figurinha',
'Davies   Canadá Figurinha',
'Pulisic   Estados Unidos Figurinha',
'Ochoa   México Figurinha',
'Keylor Navas  Costa Rica Figurinha',
'Sadio Mané  Senegal Figurinha',
'Partey   Gana Figurinha',
'Ellyes Skhiri  Tunísia Figurinha',
'André Onana  Camarões Figurinha',
'Achraf Hakimi  Marrocos Figurinha',
'Emiliano Martínez Argentina Figurinha',
'Franco Armani Argentina Figurinha',
'Juan Musso Argentina Figurinha',
'Gerónimo Rulli Argentina Figurinha',
'Gonzalo Montiel Argentina Figurinha',
'Nahuel Molina Argentina Figurinha',
'Juan Foyth Argentina Figurinha',
'Germán Pezzella Argentina Figurinha',
'Nehuén Pérez Argentina Figurinha',
'Cristian Romero Argentina Figurinha',
'Nicolás Otamendi Argentina Figurinha',
'Lisandro Martínez Argentina Figurinha',
'Marcos Senesi Argentina Figurinha',
'Nicolás Tagliafico Argentina Figurinha',
'Marcos Acuña Argentina Figurinha',
'Guido Rodríguez Argentina Figurinha',
'Alexis Mac Allister Argentina Figurinha',
'Rodrigo De Paul Argentina Figurinha',
'Exequiel Palacios Argentina Figurinha',
'Giovani Lo Celso Argentina Figurinha',
'Alejandro Gómez Argentina Figurinha',
'Ángel Di María Argentina Figurinha',
'Paulo Dybala Argentina Figurinha',
'Lautaro Martínez Argentina Figurinha',
'Julián Álvarez Argentina Figurinha',
'Joaquín Correa Argentina Figurinha',
'Nicolás González Argentina Figurinha',
'Ángel Correa Argentina Figurinha',
'Alisson Brasil Figurinha',
'Ederson Brasil Figurinha',
'Weverton Brasil Figurinha',
'Alex Sandro Brasil Figurinha',
'Alex Telles Brasil Figurinha',
'Daniel Alves Brasil Figurinha',
'Guilherme Arana Brasil Figurinha',
'Éder Militão Brasil Figurinha',
'Gabriel Magalhães Brasil Figurinha',
'Léo Ortiz Brasil Figurinha',
'Marquinhos Brasil Figurinha',
'Thiago Silva Brasil Figurinha',
'Bruno Guimarães Brasil Figurinha',
'Casemiro Brasil Figurinha',
'Danilo Brasil Figurinha',
'Fabinho Brasil Figurinha',
'Fred Brasil Figurinha',
'Lucas Paquetá Brasil Figurinha',
'Philippe Coutinho Brasil Figurinha',
'Gabriel Jesus Brasil Figurinha',
'Gabriel Martinelli Brasil Figurinha',
'Matheus Cunha Brasil Figurinha',
'Raphinha Brasil Figurinha',
'Richarlison Brasil Figurinha',
'Rodrygo Brasil Figurinha',
'Vinícius Júnior Brasil Figurinha',
'Manuel Neuer Alemanha Figurinha',
'Kevin Trapp Alemanha Figurinha',
'Oliver Baumann Alemanha Figurinha',
'Benjamin Henrichs Alemanha Figurinha',
'Thilo Kehrer Alemanha Figurinha',
'Lukas Klostermann Alemanha Figurinha',
'David Raum Alemanha Figurinha',
'Antonio Rüdiger Alemanha Figurinha',
'Niklas Süle Alemanha Figurinha',
'Nico Schlotterbeck Alemanha Figurinha',
'Jonathan Tah Alemanha Figurinha',
'Julian Brandt Alemanha Figurinha',
'Leon Goretzka Alemanha Figurinha',
'İlkay Gündoğan Alemanha Figurinha',
'Kai Havertz Alemanha Figurinha',
'Jonas Hofmann Alemanha Figurinha',
'Joshua Kimmich Alemanha Figurinha',
'Jamal Musiala Alemanha Figurinha',
'Marco Reus Alemanha Figurinha',
'Anton Stach Alemanha Figurinha',
'Karim Adeyemi Alemanha Figurinha',
'Serge Gnabry Alemanha Figurinha',
'Lukas Nmecha Alemanha Figurinha',
'Leroy Sané Alemanha Figurinha',
'Timo Werner Alemanha Figurinha'
]




for indices, jogador in enumerate(jogadores):



    while run:
        print('')
        search = jogador
        print('')
        num_of_img = 1
        print('')
        print('Downloading...')
        print('')
        links_list = []
        img_list = []
        img_index = 0
        page_number = (num_of_img // 20) * 20

        url1 = f'https://www.google.com/search?q={search}&hl=pt-BR&gbv=1&source=lnms&tbm=isch&sa=X&ved=2ahUKEwipwcKTxOfrAhUUDrkGHZ3kB5kQ_AUoAXoECB8QAw&sfr=gws&sei=g8xeX6WWO4KI5OUP1Ne2sAQ'  
        req = requests.get(url1)
        soup = BeautifulSoup(req.text, 'html.parser')

        for img in soup.find_all('img')[1:]: #getting all the 'img' tag from the html file, excelpt the google icon
            if img_index == num_of_img: 
                break
            else:
                links_list.append(img.get('src'))
                img_index += 1

        for links in links_list:
            img_list.append(requests.get(links)) #acessing the images page and storing the link in a list

        for i, img in enumerate(img_list): #converting the images into byte
            with open(f'{directory}/{indices + 1}.png', 'wb') as f: #wb = write byte
                f.write(img.content)

        for pages in range(20, page_number + 20, 20):
            img_list = []
            links_list = []

            if img_index == num_of_img:
                break
            else:
                urln = f'https://www.google.com/search?q={search}&hl=pt-BR&gbv=1&tbm=isch&ei=78xeX5PTGc_Z5OUPrsyA0A0&start={pages}&sa=N' 
                req = requests.get(urln)
                soup = BeautifulSoup(req.text, 'html.parser')

                for img in soup.find_all('img')[1:]:
                    if img_index == num_of_img:
                        break
                    else:
                        links_list.append(img.get('src'))
                        img_index += 1

                for links in links_list:
                    img_list.append(requests.get(links))

                for i, img in enumerate(img_list):
                    with open(f'{directory}/{indices+1}.png', 'wb') as f: #wb = write byte
                        f.write(img.content)
            
        print('DONE!')
        print('')
        if img_index < num_of_img:
            print(f"It was only possible to download {img_index} images")
            print('')
        if img_index == 0:
            print("Unfortunately we didn't find any image to download")
            print('')
            
        exit_question = 'Y'
        if exit_question.upper()[0] == 'Y':
            break
        else:
            print(50*'=')
            continue
    print('')
    print(50*'=')
    print("Check back often!")