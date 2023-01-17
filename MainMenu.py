import flet as ft
from flet.border import BorderSide
from flet.buttons import RoundedRectangleBorder

def MyElevetatedButton(IconImage: str, title: str,action, imagewidth : int, imageheight : int):
        e1= ft.Row([
                ft.ElevatedButton(
                content=ft.Container(
                content=ft.Column(
                    [
                        ft.Image(src=IconImage, 
                        width=imagewidth,
                        height=imageheight,                        
                        ),
                        ft.Text(title, text_align="center"),
                        
                    ],
                    horizontal_alignment="center",
                    alignment="center",
                    spacing=2,

                ),
               
            ),
               style = ft.ButtonStyle ( color={
                    "hovered": ft.colors.BLUE_ACCENT,
                    "focused": ft.colors.BLUE,
                    "": ft.colors.BLACK,
                },
                bgcolor={"focused": ft.colors.PINK_200, "": ft.colors.WHITE},
                padding={"hovered": 10},
                overlay_color=ft.colors.TRANSPARENT,
                elevation={"pressed": 0, "": 1},
                animation_duration=500,
                side={
                    "": BorderSide(1, ft.colors.BLUE),
                    "hovered": BorderSide(2, ft.colors.BLUE),
                },
                shape={
                    
                    "": RoundedRectangleBorder(radius=2),
                },

            ),on_click=action,
        ),

        ]
        )
        
        return e1



