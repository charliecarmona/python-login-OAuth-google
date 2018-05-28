# -*- coding: utf-8 -*-
from .base import OAuth2Login #importe de la clase del archivo base.py


class GoogleLogin(OAuth2Login):
  #asigancion de valores utlizadas de info y estados y direccion a serivicio de google
  config_prefix = "GOOGLE_LOGIN_"
  redirect_endpoint = "_google_login"
  state_session_key = "_google_login_state"

  #obtencion de info de cuenta del usuario
  default_scope = (
    "https://www.googleapis.com/auth/userinfo.email,"
    "https://www.googleapis.com/auth/userinfo.profile"
  )
  
  # asignacion de direcion de ingreso de gogle conectado a nuetro direccion ip del proyecto localhost
  default_redirect_path = "/login/google"

  #direcciones en uso de google las cuales proveen informacion 
  auth_url = "https://accounts.google.com/o/oauth2/auth"
  token_url = "https://accounts.google.com/o/oauth2/token"
  profile_url = "https://www.googleapis.com/oauth2/v2/userinfo"

