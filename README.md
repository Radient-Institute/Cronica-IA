# Crónica de la IA Moderna

[English version](README.en.md)

## ¿Qué es este proyecto?

**Crónica de la IA Moderna** es una crónica creada y mantenida por la comunidad de **Radient Institute** para documentar, con perspectiva histórica y narrativa, cómo la inteligencia artificial pasó del laboratorio al mainstream en un período extraordinariamente corto.

El texto cubre la era **post-ChatGPT**, desde diciembre de 2022 hasta la actualidad: el momento en que la IA dejó de ser una tecnología de nicho y se convirtió en un fenómeno cultural, económico y político global.

No es un blog ni una colección de noticias.  
Es una **crónica**: capítulos autocontenidos pero conectados, escritos con foco en lo que realmente importó, en qué orden ocurrió y por qué tuvo consecuencias.

La ambición del proyecto es simple:

> Si alguien hubiera quedado en coma en enero de 2023 y despertara hoy, este libro debería permitirle entender qué pasó con la IA en su ausencia.

El proyecto es un **documento vivo**:
- se agregan nuevos capítulos a medida que la historia continúa,
- se corrigen hechos cuando aparece información más precisa,
- se aceptan contribuciones de la comunidad.

El contenido es **libre de modificar y redistribuir** bajo licencia **CC BY 4.0**.

**Comunidad y redes**
- Web: https://cronicaia.com  
- Radient Web: https://radient.institute  
- YouTube: https://www.youtube.com/@RadientNews  
- X / Twitter: https://x.com/RadientAI  
- Discord: https://discord.gg/ducUQHQTeC  

---

## Escritura y contribución

Las contribuciones son bienvenidas, tanto en contenido como en mejoras técnicas o editoriales. Antes de contribuir, es importante entender **cómo está estructurado el proyecto y qué criterios editoriales sigue**.

### Estructura general del proyecto

El sitio está construido con **Hugo (Extended)** utilizando el tema base **hugo-book** y personalizaciones propias:  
https://github.com/alex-shpak/hugo-book

- **Contenido principal (español):** `content.es/docs/content/`
- **Traducciones opcionales (inglés):** `content.en/docs/content/`
- Los capítulos se ordenan por:
  - nombre del archivo (numeración)
  - `weight` en el front matter
- El build final se genera en `public/` (**no se edita**).

### Formato de un capítulo

Cada capítulo es un Markdown en `content.es/docs/content/`. Ejemplo mínimo:

```yaml
---
weight: 24
bookFlatSection: true
title: "24 - Título del capítulo"
image: style_1/banner_images/24_banner.webp
---
# Título visible

Texto del capítulo...
```

Notas:
- `weight` controla el orden.
- `title` se usa en el menú.
- `image` define el banner del capítulo.
- Las imágenes se referencian desde `static/`.
- Si existe traducción, duplica el archivo en `content.en/docs/content/`.

---

## Guía editorial

Las historias narradas no son contenido generado automáticamente.

- No se aceptan capítulos escritos exclusivamente por LLMs.
- La crónica debe mantener una mirada humana, con criterio, contexto y secuencia temporal.
- Tono narrativo e informativo: evita listas de titulares y “ruido”.
- La primera version no cuenta con referencias pero la meta es agregar citas y fuentes a los capítulos actuales y futuros.
- Se prefieren revisiones pequeñas y frecuentes antes que cambios masivos.

---

## Estilos visuales y assets

El proyecto utiliza tres estilos visuales: `style_1`, `style_2`, `style_3`.

- Estáticos por estilo: `static/style_X/`
- Banners: `static/style_X/banner_images/`
- SCSS: `assets/style_X/`

La selección de estilo se hace en `layouts/partials/docs/html-head.html`: elige un estilo al azar y lo guarda en `localStorage` con la clave `site-style`.  
Para fijar un estilo, cambia manualmente ese valor.

Imágenes generadas con Midjourney v7:
- `style_1`: `--sref 2661356114`
- `style_2`: `--sref 1625887214`
- `style_3`: `--sref 1782315770`

---

## Requisitos y desarrollo local

- **Requisito:** Hugo Extended  
  https://gohugo.io/installation/

- **Servidor local (en `mydocs`):**
  ```bash
  hugo server --minify --theme hugo-book
  ```
- Por defecto: http://localhost:1313/  
- Usa `--disableFastRender` si necesitas recargas completas.

---

## Flujo de contribución

- Abre issues o pull requests en: https://github.com/RadientAI/Cronica-IA
- Mantén los cambios acotados.
- Incluye capturas o previews si modificas estilos.
- Asegura un build limpio (`hugo server -D` o `hugo --minify`) antes de enviar.
- Cualquier duda o sugerencia únete a la comunidad en Discord: https://discord.gg/ducUQHQTeC
