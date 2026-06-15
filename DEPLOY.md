# Kent Tools - Deploy to GitHub Pages

## Quick Deploy (5 minutes)

### 1. Create a GitHub Repository
1. Go to https://github.com/new
2. Repository name: `kent-tools` (or any name)
3. Make it **Public** (required for free GitHub Pages)
4. Do NOT initialize with README

### 2. Push the Site
```bash
cd power-tools-site
git init
git add .
git commit -m "Initial commit - Kent Tools foreign trade site"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/kent-tools.git
git push -u origin main
```

### 3. Enable GitHub Pages
1. Go to your repo → Settings → Pages
2. Source: **Deploy from a branch**
3. Branch: `main` → `/ (root)` → Save
4. Your site will be live at `https://YOUR-USERNAME.github.io/kent-tools/`

### 4. Custom Domain (Optional)
1. Add a `CNAME` file with your domain
2. In your DNS provider, add a CNAME record pointing to `YOUR-USERNAME.github.io`
3. Enable "Enforce HTTPS" in GitHub Pages settings

## Site Structure
```
power-tools-site/
├── index.html          # Home page — hero, categories, featured products
├── products.html       # 9 rebar tools with full specs tables
├── about.html          # Company story, values, certifications
├── contact.html        # Inquiry form + WhatsApp + FAQ
├── css/style.css       # All styles (industrial blue+orange theme)
├── js/main.js          # Nav, form, animations
├── images/             # Product images from aytotech.com
└── DEPLOY.md           # This file
```

## Product Catalog (9 Items)
| # | Product | Models |
|---|---------|--------|
| 1 | Rebar Tying Tool | RT460, RT660 |
| 2 | Rebar Tying Machine | RT528, RT545, RT558 |
| 3 | Rebar Bender | C16-C36 |
| 4 | Brushless Rebar Bender | WSC16-WSC28 |
| 5 | Rebar Cutter | S18, C20 |
| 6 | Rebar Flush Cutter | F20, F30 |
| 7 | Hydraulic Rebar Cutter | A16-A32 |
| 8 | Rebar Sleeve Threading Machine | — |
| 9 | 0.8mm Tie Wire Roll | — |

## Customizing

### Contact Info (already set)
- Email: kent@gezhi.group
- WhatsApp: +995 593 583 830

### Activate the Contact Form
1. Sign up at https://formspree.io (free plan)
2. Create a new form
3. In `js/main.js`, replace `your-form-id` with your Formspree ID

### Factory Image
Replace the SVG placeholder in `about.html` (`.about-image-placeholder`) with a real factory photo.

## CloudStudio Preview
https://33af6e5fed9b4c5588d5306ae12520e5.app.codebuddy.work
