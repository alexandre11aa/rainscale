from django.core.exceptions import ValidationError


def lat_limit(latitude: float, latitude_maxima: float = 90, latitude_minima: float = -90):
    '''
    Verifica se a latitude está dentro do intervalo exigido.
    '''

    if latitude < latitude_minima or latitude > latitude_maxima:
        raise ValidationError(f"A latitude deve estar entre {latitude_minima} e {latitude_maxima} graus.")
    
def lon_limit(longitude: float, longitude_maxima: float = 180, longitude_minima: float = -180):
    '''
    Verifica se a longitude está dentro do intervalo exigido.
    '''

    if longitude < longitude_minima or longitude > longitude_maxima:
        raise ValidationError(f"A longitude deve estar entre {longitude_minima} e {longitude_maxima} graus.")