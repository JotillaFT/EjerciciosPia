from main.tarea47 import filtroInmueble, calcPrecio, compPrecio

listaInmuebles = [
    {"ano": 2000, "metros": 100, "habitacións": 3, "garaxe": True, "zona": "A"},
    {"ano": 2012, "metros": 60, "habitacións": 2, "garaxe": True, "zona": "B"},
    {"ano": 1980, "metros": 120, "habitacións": 4, "garaxe": False, "zona": "A"},
    {"ano": 2005, "metros": 75, "habitacións": 3, "garaxe": True, "zona": "B"},
    {"ano": 2015, "metros": 90, "habitacións": 2, "garaxe": False, "zona": "A"},
]


def test_funcion():
    assert filtroInmueble(listaInmuebles, 900000) == [
        {
            "ano": 2000,
            "metros": 100,
            "habitacións": 3,
            "garaxe": True,
            "zona": "A",
            "precio": 98800.0,
        },
        {
            "ano": 2012,
            "metros": 60,
            "habitacións": 2,
            "garaxe": True,
            "zona": "B",
            "precio": 112200.0,
        },
        {
            "ano": 1980,
            "metros": 120,
            "habitacións": 4,
            "garaxe": False,
            "zona": "A",
            "precio": 78400.00000000001,
        },
        {
            "ano": 2005,
            "metros": 75,
            "habitacións": 3,
            "garaxe": True,
            "zona": "B",
            "precio": 127575.0,
        },
        {
            "ano": 2015,
            "metros": 90,
            "habitacións": 2,
            "garaxe": False,
            "zona": "A",
            "precio": 91000.0,
        },
    ]


def test_comparar():
    assert (
        compPrecio(
            {"ano": 2000, "metros": 100, "habitacións": 3, "garaxe": True, "zona": "A"},
            9000000,
        )
        == True
    )


def test_precio():
    assert (
        calcPrecio(
            {"ano": 2000, "metros": 100, "habitacións": 3, "garaxe": True, "zona": "A"}
        )
        == 98800.0
    )
