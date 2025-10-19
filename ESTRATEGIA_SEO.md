# 🎯 Estrategia SEO - davidcarusso.com.ar

## 📊 Palabras clave objetivo

### Primarias (alta prioridad)
- **consultor business intelligence buenos aires** (50-100 búsquedas/mes)
- **dashboards personalizados** (100-500 búsquedas/mes)
- **consultor power bi argentina** (20-50 búsquedas/mes)
- **desarrollador streamlit** (10-50 búsquedas/mes)

### Secundarias (long-tail)
- "análisis de datos para pymes buenos aires"
- "dashboard interactivo python"
- "automatización reportes excel"
- "consultor bi zona sur buenos aires"
- "visualización de datos streamlit"

### Palabras de intención comercial
- "contratar consultor bi"
- "precio dashboard power bi"
- "consultoría business intelligence costo"

---

## 🏗️ Estructura de contenido optimizada

### Landing Page (/)
**Title:** David Carusso - Consultor BI & Dashboards | Buenos Aires
**H1:** Transformá tus datos en decisiones estratégicas
**Densidad de keywords:** 2-3% de las palabras clave principales

### Acerca de mí (/Acerca_de_mi)
**Title:** Sobre David Carusso - Analista de Datos Python y Power BI
**H1:** Acerca de mi

### Demos técnicas
Cada demo debe tener:
- Title descriptivo con keywords
- Meta description única
- H1 con keyword relevante

---

## 🔧 Mejoras técnicas implementadas

### ✅ Meta Tags
- Description optimizada (155-160 caracteres)
- Keywords relevantes
- Geo-targeting (Buenos Aires)
- Language tags

### ✅ Open Graph
- Para compartir en redes sociales
- Mejora CTR desde Facebook/LinkedIn

### ✅ Schema.org
- Tipo: ProfessionalService
- Datos estructurados para Google
- Rich snippets en resultados de búsqueda

### ✅ Canonical URL
- Evita contenido duplicado
- Consolida ranking

---

## 📈 Optimizaciones pendientes

### 1. **Performance (crítico para SEO)**

Agregá esto a tu `app.py`:

```python
# Optimización de carga
st.cache_data.clear()  # Limpiar cache periódicamente
```

**Métricas objetivo:**
- First Contentful Paint (FCP): < 1.8s
- Largest Contentful Paint (LCP): < 2.5s
- Cumulative Layout Shift (CLS): < 0.1
- Time to Interactive (TTI): < 3.8s

**Herramientas para medir:**
- [Google PageSpeed Insights](https://pagespeed.web.dev/)
- [GTmetrix](https://gtmetrix.com/)

### 2. **Imágenes optimizadas**

**Problemas actuales:**
- La imagen de LinkedIn es externa (puede ser lenta)
- No hay atributos ALT optimizados

**Solución:**
```python
st.image(
    imagen_url, 
    caption="David Carusso - Consultor Business Intelligence Buenos Aires",
    use_column_width=True
)
```

### 3. **Contenido adicional**

Creá estas páginas/secciones:

**Blog/Artículos** (para SEO de contenido):
- "Cómo elegir un dashboard para tu negocio"
- "5 métricas clave para PyMEs"
- "Power BI vs Streamlit: ¿Cuál elegir?"

**Casos de estudio** (aunque sean ficticios basados en tus demos):
- "Cómo reduje 10 horas semanales con automatización"
- "Dashboard de ventas: de Excel a visualización interactiva"

### 4. **Link Building local**

- Registrarte en Google My Business
- Directorios locales (Bumeran, Computrabajo, etc.)
- LinkedIn con link a tu sitio
- GitHub con link en el README

---

## 🎯 Google Search Console

### Pasos para configurar:

1. **Verificar propiedad:**
   - Andá a [Google Search Console](https://search.google.com/search-console)
   - Agregá `davidcarusso.com.ar`
   - Verificá con archivo HTML o DNS

2. **Subir sitemap:**
   ```
   https://davidcarusso.com.ar/sitemap.xml
   ```

3. **Monitorear:**
   - Impresiones
   - Clicks
   - CTR
   - Posición promedio

### Métricas a trackear semanalmente:

| Métrica | Objetivo Mes 1 | Objetivo Mes 3 |
|---------|----------------|----------------|
| Impresiones | 100 | 500 |
| Clicks | 10 | 50 |
| CTR | 5% | 8% |
| Posición | < 30 | < 15 |

---

## 🔍 Auditoría SEO mensual

### Checklist:

- [ ] Verificar errores 404 en Search Console
- [ ] Revisar velocidad de carga (objetivo: < 3s)
- [ ] Analizar keywords que generan tráfico
- [ ] Actualizar meta descriptions si CTR es bajo
- [ ] Revisar backlinks nuevos
- [ ] Verificar posicionamiento de keywords principales
- [ ] Actualizar sitemap con nuevas páginas

---

## 📱 SEO Local (crítico para tu caso)

### Google My Business

**Categorías:**
- Consultor de informática
- Servicios de desarrollo de software
- Analista de datos

**Descripción:**
```
Consultor de Business Intelligence especializado en dashboards interactivos 
con Python (Streamlit) y Power BI. Ayudo a PyMEs de Buenos Aires a 
transformar sus datos en decisiones estratégicas. Primera consulta gratuita.

Servicios:
• Dashboards personalizados
• Automatización de reportes
• Análisis de datos
• Power BI y Python

Zona de servicio: CABA, Zona Norte y Sur GBA
```

**Fotos a subir:**
- Tu foto profesional
- Screenshots de tus dashboards
- Logo (si tenés)

---

## 🎯 Integración con Google Ads

### Landing Page Quality Score

Para que Google Ads funcione bien, tu landing necesita:

**✅ Relevancia:**
- Keywords de los anuncios deben estar en la página
- Ya implementado: "dashboards", "business intelligence", "Python"

**✅ Experiencia de usuario:**
- CTAs claros (WhatsApp, Email) ✅
- Tiempo de carga rápido (medir con PageSpeed)
- Mobile-friendly (Streamlit ya lo es)

**✅ Velocidad:**
- Objetivo: < 3 segundos
- Crítico para Quality Score

### Tracking de conversiones

Agregá eventos de Analytics en los botones:

```javascript
// En pag_landing.py
<script>
function trackContact(type) {
    gtag('event', 'contact_click', {
        'event_category': 'engagement',
        'event_label': type,
        'value': 1
    });
}
</script>
```

Luego modificá los botones:
```python
st.markdown('<a href="https://wa.me/..." onclick="trackContact(\'whatsapp\')">WhatsApp</a>')
```

---

## 📊 KPIs de éxito

### Mes 1 (Aprendizaje)
- 50+ visitantes únicos
- 5+ clicks en WhatsApp/Email
- 1-2 consultas reales
- Bounce rate < 60%

### Mes 2-3 (Optimización)
- 150+ visitantes únicos
- 15+ clicks en contacto
- 3-5 consultas cualificadas
- Posicionamiento top 20 para 2-3 keywords

### Mes 4-6 (Escala)
- 300+ visitantes únicos
- 30+ leads
- 5-10 proyectos cerrados
- Top 10 para keywords principales

---

## 🚨 Errores a evitar

1. **Keyword stuffing:** No repitas las palabras clave de forma antinatural
2. **Contenido duplicado:** Cada página debe ser única
3. **Falta de móvil:** Streamlit ya es responsive, pero verificá
4. **Sin HTTPS:** Asegurate que tu dominio tenga SSL activo
5. **Ignorar Analytics:** Revisá datos semanalmente para optimizar

---

## 📚 Recursos útiles

- [Google Search Central](https://developers.google.com/search)
- [Ahrefs Free Tools](https://ahrefs.com/free-seo-tools)
- [Google Keyword Planner](https://ads.google.com/intl/es_ar/home/tools/keyword-planner/)
- [SEMrush (versión gratuita)](https://www.semrush.com/)

---

## ✅ Próximos pasos inmediatos

1. **Hoy:**
   - Subir robots.txt y sitemap.xml
   - Verificar dominio en Google Search Console
   - Configurar Google Analytics

2. **Esta semana:**
   - Medir velocidad de carga
   - Optimizar imágenes
   - Verificar mobile-friendliness

3. **Este mes:**
   - Crear 2-3 artículos de blog
   - Registrarse en Google My Business
   - Conseguir primeros backlinks (LinkedIn, GitHub)

4. **Próximos 3 meses:**
   - Publicar 1 caso de estudio/mes
   - Construir 5-10 backlinks locales
   - Optimizar según datos de Search Console