from pywebio.input import *
from pywebio.output import *
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
import argparse
from pywebio import start_server, session
from menu import Menu


mymenu= Menu()  # obj of class Menu
header_img = open('images/NITTE.svg', 'rb').read()

app= Flask(__name__)

def main_func():
    session.set_env(title='Nucat - 2024', output_animation=False)

    mymenu.user=None
    while(mymenu.user!=4):  # end program when option 4 i.e. exit portal is selected.
        mymenu.login()
        if mymenu.user==2:
            mymenu.menu_for_student()
        elif mymenu.user==3:
            mymenu.menu_for_admin()

    with use_scope('ROOT'):
        put_image(header_img, width='100%', height='40px', position=0)
        put_info("Thank you for visiting our site.", position=1)

        clear("main")        

app.add_url_rule('/', 'webio_view', webio_view(main_func), methods=['GET','POST','OPTIONS'])

if __name__== '__main__':
    parser= argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args= parser.parse_args()
    start_server(main_func, port= args.port, websocket_ping_interval= 60)

#app.run(host='Localhost', port=80) 

# visit http://localhost/tool to open the application
