# Study: session

## django html templates

```python
TEMPLATES = [
    {
        'DIRS': [os.path.join(BASE_DIR, 'survey_project', 'templates')],
        'APP_DIRS': True,
    },
]
```

## session

```python
@login_required
def index(request):
    request.session['visit_num'] = request.session.get('visit_num', 0) + 1
    request.session.modified = True

    context = {
        'visit_num': visit_num
    }

    return render(request, 'todo/index.html', context)
```
