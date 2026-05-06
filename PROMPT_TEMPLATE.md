# Шаблон промпта для Perplexity — создание новой презентации VTech

Копируй и вставляй этот промпт в Perplexity, подставляя свои данные:

---

```
Ты — агент по созданию презентаций для технобренда VTech.

Гитхаб-репозиторий: https://github.com/olegbuselru/vtech-presentations

Твоя задача:
1. Прочитай файл DESIGN.md из этого репозитория (он содержит все правила дизайна VTech)
2. Создай новую HTML-презентацию на Reveal.js в точном соответствии с дизайн-системой VTech
3. Создай файл meta.json с метаданными
4. Сделай Pull Request в репозиторий — добавь папку presentations/YYYY-MM-DD-slug/

ПАРАМЕТРЫ НОВОЙ ПРЕЗЕНТАЦИИ:
- Тема: [ВСТАВЬ ТЕМУ]
- Ивент: [НАЗВАНИЕ МИТАПА / КОНФЕРЕНЦИИ]
- Дата: [ДАТА]
- Ключевые тезисы: [3-5 КЛЮЧЕВЫХ ИДЕИ]
- Количество слайдов: ~12-15
- Теги: [СПИСОК ТЕГОВ]

Строго следуй DESIGN.md: тёмный фон #0A0E1A, акцент #00F5C4, шрифты Space Grotesk + Inter, Reveal.js.
Название папки: YYYY-MM-DD-slug (slug = транслит темы латиницей, через дефис).
```

---

## Что получишь на выходе:
- PR с новой презентацией в папке `presentations/`
- После merge → автоматический деплой через GitHub Actions
- Карточка появится на главной странице сайта

## Ссылки:
- Сайт: https://olegbuselru.github.io/vtech-presentations
- Репо: https://github.com/olegbuselru/vtech-presentations
- DESIGN.md: https://github.com/olegbuselru/vtech-presentations/blob/main/DESIGN.md
