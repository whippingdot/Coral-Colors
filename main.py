import reflux

t = reflux.Theme({
    "name": "DE DOORK BALUE",
    "author": "Whippingdot",
    "description": "loot of doork balue",
    "default": "dark"
})

t.set_colors({
    "border": "#233D4D",

    "control-1": "#008DA3",
    "control-2": "#00B1CC",
    "control-3": "#33E4FF",

    "primary-1": "#0FF4C6",
    "primary-2": "#44FFD2",
    "primary-3": "#70EE9C",
    "primary-4": "#6FEDB7",

    "background-1": "#1A5E63",
    "background-2": "#278A91",
    "background-3": "#33B8C1",
    "background-4": "#4EC7D0"
})

t.build("theme.min.js", "w+")
