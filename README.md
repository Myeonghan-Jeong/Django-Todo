# Todo app with login

### Setting template directory

```python
TEMPLATES = [
    {
        'DIRS': [os.path.join(BASE_DIR, 'wunderlist', 'templates')],

        'APP_DIRS': True,
    },
]
```

### HTML session

```python
@login_required
def index(request):

    visit_num = request.session.get('visit_num', 0)

    request.session['visit_num'] = visit_num + 1
    request.session.modified = True

    context = {
        'visit_num': visit_num
    }

    return render(request, 'todos/index.html', context)
```
