
---

### 📄 `update.md`
```markdown
# Update Book Instance

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book
# Expected Output:
# <Book: Nineteen Eighty-Four by George Orwell (1949)>
