TOP_10_FEATURES = [
    "OPERA_American Airlines",
    "OPERA_Avianca",
    "OPERA_Air Canada",
    "MES_7",
    "MES_12",
    "OPERA_Qantas Airways",
    "OPERA_Latin American Wings",
    "OPERA_Gol Trans",
    "OPERA_Copa Air",
    "TIPOVUELO_I",
]

THRESHOLD_IN_MINUTES = 15
MODEL_PKL = "logistic_regression_model-rc-0-0-1.pkl"


FEATURE_DOMAIN = {
    "OPERA": ['American Airlines', 'Air Canada', 'Air France', 'Aeromexico',
       'Aerolineas Argentinas', 'Austral', 'Avianca', 'Alitalia',
       'British Airways', 'Copa Air', 'Delta Air', 'Gol Trans', 'Iberia',
       'K.L.M.', 'Qantas Airways', 'United Airlines', 'Grupo LATAM',
       'Sky Airline', 'Latin American Wings', 'Plus Ultra Lineas Aereas',
       'JetSmart SPA', 'Oceanair Linhas Aereas', 'Lacsa'],
    "TIPOVUELO": ["I", "N"],
    "SIGLADES": ['Miami', 'Dallas', 'Buenos Aires', 'Toronto', 'Paris',
       'Ciudad de Mexico', 'Bogota', 'Roma', 'Londres',
       'Ciudad de Panama', 'Atlanta', 'Sao Paulo', 'Rio de Janeiro',
       'Florianapolis', 'Madrid', 'Lima', 'Sydney', 'Houston', 'Asuncion',
       'Cataratas Iguacu', 'Puerto Montt', 'Punta Arenas',
       'Puerto Natales', 'Balmaceda', 'Temuco', 'Valdivia', 'Concepcion',
       'La Serena', 'Copiapo', 'Calama', 'Antofagasta', 'Iquique',
       'Arica', 'Mendoza', 'Cordoba', 'Montevideo', 'Castro (Chiloe)',
       'Osorno', 'Orlando', 'Nueva York', 'Guayaquil', 'Cancun',
       'Punta Cana', 'Los Angeles', 'Auckland N.Z.', 'Isla de Pascua',
       'La Paz', 'Santa Cruz', 'Curitiba, Bra.', 'Quito', 'Bariloche',
       'Rosario', 'Washington', 'Tucuman', 'Melbourne', 'San Juan, Arg.',
       'Neuquen', 'Pisco, Peru', 'Ushuia', 'Puerto Stanley',
       'Punta del Este', 'Cochabamba'],
    "MES": [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12],
    "DIANOM": ['Domingo', 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Sabado', 'Viernes']   
}


