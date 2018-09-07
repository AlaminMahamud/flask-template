# Project Structure For Flask Application
```bash
read NEW_PROJECT_NAME
git clone git@github.com:nprapps/app-template.git $NEW_PROJECT_NAME
cd $NEW_PROJECT_NAME

mkvirtualenv $NEW_PROJECT_NAME
pip install -r requirements.txt
npm install

#fab bootstrap
```
## Flask
1. Render Jinja HTML templates on demand
2. Compile LESS into CSS
3. Compile individual JST templates into a single file called templates.js
4. Compile app_config.py into app_config.js so our application configuration is also available in JavaScript

## Asset Pipeline
When we deploy, we push all our CSS into one file and all of our JS into a single file. We then gzip all of these assets for production (we only gzip, not minify, to avoid obfuscation).


```javascript
<!-- CSS -->
{{ CSS.push('css/bootstrap.css') }}
{{ CSS.push('css/bootstrap-responsive.css') }}
{{ CSS.push('less/app.less') }}
{{ CSS.render('css/app.min.css') }}


<!-- JS  -->
{{ JS.push('js/app_config.js') }}
{{ JS.push('js/console.js') }}
{{ JS.push('js/lib/jquery-1.8.3.js') }}
{{ JS.push('js/lib/modernizr.js') }}
{{ JS.push('js/responsive-ad.js') }}
{{ JS.render('js/app-header.min.js') }}
```