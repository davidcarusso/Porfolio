"""
Script para verificar elementos SEO básicos de la landing page
Uso: python scripts/check_seo.py
"""

import re
from pathlib import Path

def check_file_exists(filepath):
    """Verifica si un archivo existe"""
    return Path(filepath).exists()

def analyze_meta_tags(content):
    """Analiza meta tags en el contenido"""
    checks = {
        "Meta Description": bool(re.search(r'<meta name="description"', content)),
        "Meta Keywords": bool(re.search(r'<meta name="keywords"', content)),
        "Open Graph": bool(re.search(r'<meta property="og:', content)),
        "Schema.org": bool(re.search(r'<script type="application/ld\+json">', content)),
        "Canonical URL": bool(re.search(r'<link rel="canonical"', content)),
    }
    return checks

def check_heading_structure(content):
    """Verifica estructura de headings"""
    h1_count = len(re.findall(r'<h1|# ', content))
    h2_count = len(re.findall(r'<h2|## ', content))
    
    return {
        "H1 presente": h1_count > 0,
        "H1 único": h1_count == 1,
        "H2 presentes": h2_count > 0
    }

def analyze_keyword_density(content, keywords):
    """Analiza densidad de palabras clave"""
    content_lower = content.lower()
    total_words = len(content_lower.split())
    
    results = {}
    for keyword in keywords:
        count = content_lower.count(keyword.lower())
        density = (count / total_words) * 100 if total_words > 0 else 0
        results[keyword] = {
            "count": count,
            "density": round(density, 2)
        }
    return results

def main():
    print("🔍 SEO Checker - davidcarusso.com.ar\n")
    print("=" * 50)
    
    # Archivos a verificar
    files_to_check = {
        "Landing Page": "views/pag_landing.py",
        "robots.txt": "robots.txt",
        "sitemap.xml": "sitemap.xml"
    }
    
    print("\n📁 Verificando archivos...\n")
    for name, filepath in files_to_check.items():
        exists = check_file_exists(filepath)
        status = "✅" if exists else "❌"
        print(f"{status} {name}: {filepath}")
    
    # Analizar landing page
    landing_path = "views/pag_landing.py"
    if check_file_exists(landing_path):
        print("\n" + "=" * 50)
        print("📊 Análisis de Landing Page\n")
        
        with open(landing_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Meta tags
        print("🏷️  Meta Tags:")
        meta_checks = analyze_meta_tags(content)
        for check, passed in meta_checks.items():
            status = "✅" if passed else "❌"
            print(f"  {status} {check}")
        
        # Estructura de headings
        print("\n📝 Estructura de Headings:")
        heading_checks = check_heading_structure(content)
        for check, passed in heading_checks.items():
            status = "✅" if passed else "❌"
            print(f"  {status} {check}")
        
        # Densidad de keywords
        print("\n🎯 Densidad de Keywords:")
        keywords = [
            "business intelligence",
            "dashboard",
            "streamlit",
            "power bi",
            "datos"
        ]
        keyword_analysis = analyze_keyword_density(content, keywords)
        for keyword, data in keyword_analysis.items():
            density_status = "✅" if 1 <= data["density"] <= 3 else "⚠️"
            print(f"  {density_status} '{keyword}': {data['count']} veces ({data['density']}%)")
        
        print("\n💡 Recomendación: Densidad ideal entre 1-3%")
    
    # Verificar HTTPS
    print("\n" + "=" * 50)
    print("🔒 Recordatorios:\n")
    print("  ⚠️  Verificar que el dominio tenga HTTPS activo")
    print("  ⚠️  Configurar Google Search Console")
    print("  ⚠️  Instalar Google Analytics")
    print("  ⚠️  Medir velocidad con PageSpeed Insights")
    
    print("\n" + "=" * 50)
    print("✅ Análisis completado\n")

if __name__ == "__main__":
    main()