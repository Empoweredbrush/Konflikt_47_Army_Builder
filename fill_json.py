import json
import fitz
import requests


Factions = [
    {
    "name": "Axis",
    "url": "https://warlord-community.warlordgames.com/wp-content/uploads/2026/03/K47_Army-List_Axis_MAR2026.pdf",
    "output": "k47ArmyData.json"
    },
    {
        "name": "British",
        "url": "https://warlord-community.warlordgames.com/wp-content/uploads/2026/03/K47_Army-List_British-Commonwealth_MAR2026.pdf",
        "output": "k47ArmyData.json"
    },
    {
        "name": "Japan",
        "url": "https://warlord-community.warlordgames.com/wp-content/uploads/2026/03/K47_Army-List_Japan_MAR2026.pdf",
        "output": "k47ArmyData.json"
    },
    {
        "name": "USA",
        "url": "https://warlord-community.warlordgames.com/wp-content/uploads/2026/03/K47_Army-List_USA_240326.pdf",
        "output": "k47ArmyData.json"
    },
    {
        "name": "Soviet",
        "url": "https://warlord-community.warlordgames.com/wp-content/uploads/2026/03/K47_Army-List_Soviet_MAR2026.pdf",
        "output": "k47ArmyData.json"
    }
]

