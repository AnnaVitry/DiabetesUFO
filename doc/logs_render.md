1. Logs déploiement Render du front:

URL front: `https://diabetesufo-1.onrender.com/`

```bash
2025-10-21T10:06:59.085455246Z ==> Deploying...
2025-10-21T10:07:57.932082702Z ==> Running 'streamlit run app.py'
2025-10-21T10:08:02.240894478Z 
2025-10-21T10:08:02.240919839Z Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.
2025-10-21T10:08:02.240923929Z 
2025-10-21T10:08:04.349609921Z 
2025-10-21T10:08:04.349660452Z   You can now view your Streamlit app in your browser.
2025-10-21T10:08:04.349667122Z 
2025-10-21T10:08:04.349713103Z   Local URL: http://localhost:8501
2025-10-21T10:08:04.349718723Z   Network URL: http://10.16.52.238:8501
2025-10-21T10:08:04.349722873Z   External URL: http://54.254.162.138:8501
2025-10-21T10:08:04.349798495Z 
2025-10-21T10:08:05.093864796Z ==> No open ports detected, continuing to scan...
2025-10-21T10:08:06.069562284Z ==> Docs on specifying a port: https://render.com/docs/web-services#port-binding
2025-10-21T10:08:45.948664562Z ==> New primary port detected: 8501. Restarting deploy to update network configuration...
2025-10-21T10:08:46.515792057Z ==> Docs on specifying a port: https://render.com/docs/web-services#port-binding
2025-10-21T10:09:08.139332827Z ==> Running 'streamlit run app.py'
2025-10-21T10:09:14.655544945Z 
2025-10-21T10:09:14.655566465Z Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.
2025-10-21T10:09:14.655569846Z 
2025-10-21T10:09:17.288671051Z ==> Your service is live 🎉
2025-10-21T10:09:17.475760197Z ==> 
2025-10-21T10:09:17.526377097Z 
2025-10-21T10:09:17.526401388Z   You can now view your Streamlit app in your browser.
2025-10-21T10:09:17.526418749Z 
2025-10-21T10:09:17.52646219Z   Local URL: http://localhost:8501
2025-10-21T10:09:17.526539031Z   Network URL: http://10.16.52.196:8501
2025-10-21T10:09:17.526552872Z   External URL: http://54.254.162.138:8501
2025-10-21T10:09:17.526567302Z 
2025-10-21T10:09:17.659729754Z ==> ///////////////////////////////////////////////////////////
2025-10-21T10:09:17.845366271Z ==> 
2025-10-21T10:09:18.463469506Z ==> Available at your primary URL https://diabetesufo-1.onrender.com
2025-10-21T10:09:19.09279209Z ==> 
2025-10-21T10:09:19.283312847Z ==> ///////////////////////////////////////////////////////////
2025-10-21T10:09:33.631894538Z 2025-10-21 10:09:33.630 Uncaught app exception
2025-10-21T10:09:33.631914269Z Traceback (most recent call last):
2025-10-21T10:09:33.631920399Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 589, in _run_script
2025-10-21T10:09:33.631926819Z     exec(code, module.__dict__)
2025-10-21T10:09:33.631931209Z     ~~~~^^^^^^^^^^^^^^^^^^^^^^^
2025-10-21T10:09:33.631935639Z   File "/opt/render/project/src/app/front/app.py", line 117, in <module>
2025-10-21T10:09:33.631939949Z     response = requests.post(API_URL+"/predict", json=user_input)
2025-10-21T10:09:33.631944059Z                              ~~~~~~~^~~~~~~~~~~
2025-10-21T10:09:33.63194872Z TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'
2025-10-21T10:09:51.759483587Z ==> Detected a new open port HTTP:8501
2025-10-21T10:10:16.88129981Z   Stopping...
2025-10-21T10:11:01.546530246Z     exec(code, module.__dict__)
2025-10-21T10:11:01.546534516Z     ~~~~^^^^^^^^^^^^^^^^^^^^^^^
2025-10-21T10:11:01.546539696Z   File "/opt/render/project/src/app/front/app.py", line 117, in <module>
2025-10-21T10:11:01.546544306Z     response = requests.post(API_URL+"/predict", json=user_input)
2025-10-21T10:11:01.546548726Z                              ~~~~~~~^~~~~~~~~~~
2025-10-21T10:11:01.546553506Z TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'
2025-10-21T10:13:28.718100634Z ==> Deploying...
2025-10-21T10:14:06.129858719Z ==> Running 'streamlit run app.py'
2025-10-21T10:14:10.93558234Z 
2025-10-21T10:14:10.935608711Z Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.
2025-10-21T10:14:10.935613431Z 
2025-10-21T10:14:14.64100819Z 
2025-10-21T10:14:14.641040542Z   You can now view your Streamlit app in your browser.
2025-10-21T10:14:14.641046872Z 
2025-10-21T10:14:14.641066563Z   Local URL: http://localhost:8501
2025-10-21T10:14:14.641072653Z   Network URL: http://10.16.121.108:8501
2025-10-21T10:14:14.641093824Z   External URL: http://54.254.162.138:8501
2025-10-21T10:14:14.641099654Z 
2025-10-21T10:14:21.432089817Z ==> Your service is live 🎉
2025-10-21T10:14:21.620146873Z ==> 
2025-10-21T10:14:21.80323817Z ==> ///////////////////////////////////////////////////////////
2025-10-21T10:14:21.988353276Z ==> 
2025-10-21T10:14:22.200424891Z ==> Available at your primary URL https://diabetesufo-1.onrender.com
2025-10-21T10:14:22.426115995Z ==> 
2025-10-21T10:14:22.63257522Z ==> ///////////////////////////////////////////////////////////
2025-10-21T10:15:19.38770562Z   Stopping...
2025-10-21T10:19:21.948775569Z ==> Detected service running on port 8501
2025-10-21T10:19:22.48020907Z ==> Docs on specifying a port: https://render.com/docs/web-services#port-binding
2025-10-21T10:26:13.983513822Z ==> Deploying...
2025-10-21T10:26:54.865269279Z ==> Running 'streamlit run app.py'
2025-10-21T10:26:59.235407887Z 
2025-10-21T10:26:59.235430417Z Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.
2025-10-21T10:26:59.235434807Z 
2025-10-21T10:27:00.639453478Z 
2025-10-21T10:27:00.639479179Z   You can now view your Streamlit app in your browser.
2025-10-21T10:27:00.639482009Z 
2025-10-21T10:27:00.639503729Z   Local URL: http://localhost:8501
2025-10-21T10:27:00.6395109Z   Network URL: http://10.16.234.160:8501
2025-10-21T10:27:00.63953252Z   External URL: http://54.254.162.138:8501
2025-10-21T10:27:00.6395389Z 
2025-10-21T10:27:04.924358011Z ==> Your service is live 🎉
2025-10-21T10:27:05.120438576Z ==> 
2025-10-21T10:27:05.310435862Z ==> ///////////////////////////////////////////////////////////
2025-10-21T10:27:05.503346247Z ==> 
2025-10-21T10:27:05.697077573Z ==> Available at your primary URL https://diabetesufo-1.onrender.com
2025-10-21T10:27:06.570556347Z ==> 
2025-10-21T10:27:07.601441Z ==> ///////////////////////////////////////////////////////////
2025-10-21T10:28:04.481809371Z   Stopping...
2025-10-21T10:29:14.684831585Z ==> Deploying...
```

---
2. Logs de déploiement Render de l'API:

URL API: `https://diabetesufo.onrender.com/docs`

```bash
2025-10-21T10:19:05.540008817Z ==> Deploying...
2025-10-21T10:19:40.73112223Z ==> Running 'fastapi run api.py'
2025-10-21T10:19:51.631837243Z 
2025-10-21T10:19:51.632550881Z    FastAPI   Starting production server 🚀
2025-10-21T10:19:51.634861576Z  
2025-10-21T10:19:51.635670376Z              Searching for package file structure from directories with         
2025-10-21T10:19:51.635686526Z              __init__.py files                                                  
2025-10-21T10:20:09.336673121Z              Importing from /opt/render/project/src/app/api
2025-10-21T10:20:09.336881766Z  
2025-10-21T10:20:09.337596383Z     module   🐍 api.py
2025-10-21T10:20:09.33791138Z  
2025-10-21T10:20:09.338526195Z       code   Importing the FastAPI app object from the module with the following
2025-10-21T10:20:09.338555566Z              code:                                                              
2025-10-21T10:20:09.338779321Z  
2025-10-21T10:20:09.339442347Z              from api import app
2025-10-21T10:20:09.339677373Z  
2025-10-21T10:20:09.340213876Z        app   Using import string: api:app
2025-10-21T10:20:09.340421041Z  
2025-10-21T10:20:09.341507957Z     server   Server started at http://0.0.0.0:10000
2025-10-21T10:20:09.341517897Z     server   Documentation at http://0.0.0.0:10000/docs
2025-10-21T10:20:09.341752583Z  
2025-10-21T10:20:09.342170813Z              Logs:
2025-10-21T10:20:09.342358658Z  
2025-10-21T10:20:10.042448496Z       INFO   Started server process [62]
2025-10-21T10:20:10.042857926Z       INFO   Waiting for application startup.
2025-10-21T10:20:10.043518722Z       INFO   Application startup complete.
2025-10-21T10:20:10.131069168Z       INFO   Uvicorn running on http://0.0.0.0:10000 (Press CTRL+C to quit)
2025-10-21T10:20:10.247767404Z       INFO   127.0.0.1:47360 - "HEAD / HTTP/1.1" 405
2025-10-21T10:20:11.816313744Z ==> No open ports detected, continuing to scan...
2025-10-21T10:20:12.581713333Z ==> Docs on specifying a port: https://render.com/docs/web-services#port-binding
2025-10-21T10:20:17.452863262Z ==> Your service is live 🎉
2025-10-21T10:20:17.643494258Z ==> 
2025-10-21T10:20:17.843753614Z ==> ///////////////////////////////////////////////////////////
2025-10-21T10:20:18.063387078Z ==> 
2025-10-21T10:20:18.265989093Z ==> Available at your primary URL https://diabetesufo-api.onrender.com
2025-10-21T10:20:18.452239299Z ==> 
2025-10-21T10:20:18.638672876Z ==> ///////////////////////////////////////////////////////////
2025-10-21T10:20:21.643420495Z       INFO   34.82.80.145:0 - "GET / HTTP/1.1" 200
2025-10-21T10:25:20.591770809Z ==> Detected service running on port 10000
2025-10-21T10:25:21.214380483Z ==> Docs on specifying a port: https://render.com/docs/web-services#port-binding
```
