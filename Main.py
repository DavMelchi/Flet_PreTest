import flet as ft
from MainMenu import MyElevetatedButton

def main(page: ft.Page):

    def ButtonClick():
        print("OK")



    MenuPrincipal = ft.Row([  
        
            MyElevetatedButton(
                f"/assets/home.svg",
                "Button1",
                ButtonClick,
                60,
                30,
            ),
            

         
             MyElevetatedButton(
                f"/assets/home.svg",
                "Button2",
                ButtonClick,
                60,
                30,
                
            ),

            
            MyElevetatedButton(
                f"/assets/home.svg",
                "Button3",
                ButtonClick,
                60,
                30,
                
            ),
            MyElevetatedButton(
                f"/assets/home.svg",
                "Button4",
                ButtonClick,
                60,
                30
                
                
            ),
             MyElevetatedButton(
                f"/assets/home.svg",
                "Button5",
                ButtonClick,
                60,
                30,
                
            ),

            ],
                width=1200,
                height=70,
                alignment="center",
                visible= True,
                        )
    page.add(MenuPrincipal)

if __name__ == '__main__':
    ft.app(target=main,assets_dir="assets",
            )