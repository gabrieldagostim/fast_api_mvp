from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory='templates')


DOGS = [{'name':'euro', 'type': 'pastor alemao'},
        {'name':'cafe', 'type': 'doberman'}]


GUERRILHA = [
    {'name': 'IC10',
     'produtos_mapeados': [
         {'codigo': '123456',
          'descricao': 'Leite Tirol 1L',
          'capacidade_movel': 300,
          'venda30d': 600,
          'perc_particip': 0.6,
          'qtde_exp': 180,  # 300 * 0.6
          },
         {'codigo': '789012',
          'descricao': 'Café Pilão 500g',
          'capacidade_movel': 200,
          'venda30d': 400,
          'perc_particip': 0.3,
          'qtde_exp': 60,  # 200 * 0.3
          },
         {'codigo': '345678',
          'descricao': 'Arroz Tio João 5kg',
          'capacidade_movel': 100,
          'venda30d': 200,
          'perc_particip': 0.1,
          'qtde_exp': 10,  # 100 * 0.1
          },
     ]},
    {'name': 'IC20',
     'produtos_mapeados': [
         {'codigo': '654321',
          'descricao': 'Suco de Laranja 1L',
          'capacidade_movel': 150,
          'venda30d': 300,
          'perc_particip': 0.5,
          'qtde_exp': 75,  # 150 * 0.5
          },
         {'codigo': '987654',
          'descricao': 'Biscoito Cream Cracker 400g',
          'capacidade_movel': 250,
          'venda30d': 500,
          'perc_particip': 0.4,
          'qtde_exp': 100,  # 250 * 0.4
          },
         {'codigo': '567890',
          'descricao': 'Azeite de Oliva 500ml',
          'capacidade_movel': 50,
          'venda30d': 100,
          'perc_particip': 0.1,
          'qtde_exp': 5,  # 50 * 0.1
          },
     ]}
]

@app.get('/')
async def name(request: Request):
    return templates.TemplateResponse('home.html', {'request': request, 'name': 'gabriel', "dogs":DOGS})  


@app.get('/analise')
async def analise(request: Request):
    return templates.TemplateResponse('analise_guerrilha.html', {'request': request, 'guerrilha': GUERRILHA})