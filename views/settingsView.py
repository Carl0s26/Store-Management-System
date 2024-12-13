import flet as ft
import pygame # pip install pygame


pygame.mixer.init()
pygame.mixer.music.load("assets/backgroundMusic.mp3")
pygame.mixer.music.play(-1)  # loop
pygame.mixer.music.set_volume(0.2) 

def volumeChange(volume):
    pygame.mixer.music.set_volume(volume)

def settings_View(router):
    #* defining view content

    content = ft.Container(content=
        ft.Column([
            ft.Text("Contact info: 809-214-8977", size=30),
            ft.Text("operational hours: 7am - 10pm", size=30),
            ft.Text("Clear Cart", size=30),
            ft.TextField(
                label="Delivery Instruction",
                multiline=True,
                value="\n\n\n\n\n",text_size=15),
            ft.Text("Music",size=25),
            ft.Slider(
                min=0,
                max=0.2,
                value=0.1,
                divisions=10,
                on_change=lambda e: volumeChange(e.control.value),
            ),
            ft.FilledButton(text="Save button"),
        ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,)
    ,alignment=ft.alignment.center)
    return content