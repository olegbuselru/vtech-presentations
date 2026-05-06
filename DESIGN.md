# VTech Brand Design System

> Официальный дизайн-гайд технобренда VTech.
> Используется агентами для генерации новых презентаций в едином стиле.

---

## 🎨 Цветовая палитра

| Роль | Hex | OKLCH | Описание |
|------|-----|-------|----------|
| Primary | `#0A0E1A` | `oklch(0.10 0.02 250)` | Основной тёмный фон |
| Secondary | `#0D1B2A` | `oklch(0.14 0.04 240)` | Карточки и секции |
| Accent | `#00F5C4` | `oklch(0.87 0.18 175)` | Неон-минт, главный акцент |
| Accent Alt | `#7B61FF` | `oklch(0.58 0.22 280)` | Фиолетовый для тегов |
| Text Primary | `#E8ECEF` | `oklch(0.92 0.01 240)` | Основной текст |
| Text Muted | `#8899A6` | `oklch(0.58 0.03 220)` | Второстепенный текст |
| Divider | `#1E2D3D` | `oklch(0.20 0.04 235)` | Разделители и бордеры |

---

## 🔤 Типографика

```css
--font-display: 'Space Grotesk', 'Inter', sans-serif;  /* Заголовки */
--font-body:    'Inter', 'Helvetica Neue', sans-serif;  /* Основной текст */
--font-mono:    'JetBrains Mono', 'Fira Code', monospace; /* Код */
```

### Размеры
- **Hero title**: `clamp(2.5rem, 5vw, 5rem)` — Space Grotesk Bold
- **Section heading**: `clamp(1.5rem, 3vw, 2.5rem)` — Space Grotesk SemiBold
- **Body**: `1rem / 1.7` — Inter Regular
- **Caption**: `0.875rem` — Inter, цвет Text Muted

---

## 📐 Сетка и отступы

- Контентная ширина: `max-width: 1200px`
- Боковые отступы: `clamp(1rem, 5vw, 3rem)`
- Гап между карточками: `1.5rem`
- Скругление карточек: `12px`
- Секции: `padding-block: clamp(4rem, 8vw, 8rem)`

---

## ✨ Визуальный стиль

- **Тема**: Тёмный фон (dark-only), техно-минималистичный
- **Эффекты**: Subtle glow от акцентного цвета на hover, backdrop blur на оверлеях
- **Бордеры**: `1px solid oklch(from #00F5C4 l c h / 0.15)` — полупрозрачный минт
- **Тени**: `0 0 40px oklch(0.87 0.18 175 / 0.08)` — мягкий неон-глоу
- **Теги**: Капслок, `letter-spacing: 0.08em`, маленький размер, акцентный цвет

---

## 🧩 Структура презентации (формат HTML)

Каждая презентация — это отдельный `.html` файл в папке `presentations/`.

```
presentations/
  YYYY-MM-DD-slug/
    index.html      ← сама презентация (Reveal.js или кастомная)
    meta.json       ← метаданные (см. ниже)
    cover.jpg       ← превью 1200×630px (опционально)
```

### Формат `meta.json`

```json
{
  "title": "Название презентации",
  "description": "Краткое описание в 1-2 предложения",
  "date": "2026-05-06",
  "tags": ["DevRel", "AI", "Community"],
  "event": "Ви.Tech Meetup #5",
  "slides_count": 18,
  "cover": "cover.jpg"
}
```

---

## 🤖 Инструкции для AI-агента (Perplexity)

При создании новой презентации агент должен:

1. Прочитать этот `DESIGN.md` из репозитория
2. Создать папку `presentations/YYYY-MM-DD-slug/`
3. Сгенерировать `index.html` — презентацию в стиле VTech (Reveal.js)
4. Создать `meta.json` с метаданными
5. Отправить Pull Request в ветку `main`
6. GitHub Actions автоматически деплоит после merge

### Обязательный стиль:
- Тёмный фон `#0A0E1A`
- Акцент `#00F5C4` для выделений, заголовков разделов
- Шрифты: Space Grotesk (заголовки) + Inter (тело)
- Логотип VTech в левом верхнем углу каждого слайда
- Номер слайда + общее количество в правом нижнем углу
