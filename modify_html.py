from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

# Find the projects container
projects_container = soup.find('div', class_='row g-4 mt-4')
cards = projects_container.find_all('div', class_='col-lg-4 col-md-6', recursive=False)

# We want to remove the last card (Submission Coding Camp)
if len(cards) == 6:
    cards[-1].decompose()

# Create the new Odoo Card
odoo_card_html = """
<div class="col-lg-4 col-md-6" data-aos="fade-up" data-aos-delay="50">
  <div class="card card-project h-100" data-tilt data-tilt-max="5" data-tilt-glare="true" data-tilt-max-glare="0.2">
    <div class="img-wrapper">
      <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=600&q=80" class="card-img-top" alt="Odoo ERP Development" />
    </div>
    <div class="card-body d-flex flex-column">
      <h5 class="card-title fw-bold">Odoo Custom Modules</h5>
      <p class="card-text text-white-50">Kumpulan pengembangan dan modifikasi modul Odoo ERP tingkat lanjut untuk mengotomatisasi proses bisnis.</p>
      <div class="tech-tags mt-auto mb-3"><span class="badge">Odoo</span><span class="badge">Python</span><span class="badge">XML</span><span class="badge">PostgreSQL</span></div>
      <button class="btn btn-custom align-self-start" data-bs-toggle="modal" data-bs-target="#projectModalOdoo"><i class="bi bi-search"></i> Lihat Detail</button>
    </div>
  </div>
</div>
"""
odoo_card = BeautifulSoup(odoo_card_html, 'html.parser')

# Insert at the beginning of the container
projects_container.insert(0, odoo_card)

# Now, let's remove Modal 6
modal6 = soup.find('div', id='projectModal6')
if modal6:
    modal6.decompose()

# Add Modal Odoo right before the Back to Top button
odoo_modal_html = """
<div class="modal fade" id="projectModalOdoo" tabindex="-1" aria-labelledby="projectModalOdooLabel" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered modal-lg">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="projectModalOdooLabel">Odoo Custom Modules & Architecture</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80" class="img-fluid rounded mb-4" alt="Odoo Project Detail" />
        <h6>Deskripsi Proyek</h6>
        <p class="text-white-50">
          Repositori portofolio ini berisi berbagai kumpulan modul kustom Odoo yang dirancang untuk mengatasi masalah bisnis spesifik. Mulai dari penyesuaian tampilan (QWeb Views), pembuatan model baru, manipulasi ORM tingkat lanjut, hingga otomasi alur kerja (Workflows) dan API Integration.
        </p>
        <h6 class="mt-4">Fitur & Fokus Pengembangan:</h6>
        <ul class="text-white-50">
          <li>Customisasi modul inti (Sales, Inventory, Invoicing).</li>
          <li>Pengembangan report menggunakan QWeb & PDF.</li>
          <li>Implementasi business logic via Python ORM (compute fields, onchange, constraints).</li>
          <li>Mendesain interface (XML Views & Actions).</li>
        </ul>
        <h6 class="mt-4">Teknologi:</h6>
        <div class="tech-tags"><span class="badge">Odoo Framework</span><span class="badge">Python</span><span class="badge">XML / QWeb</span><span class="badge">PostgreSQL</span></div>
      </div>
      <div class="modal-footer">
        <a href="https://github.com/tatatacicici/odoo-repo-porto" target="_blank" rel="noopener noreferrer" class="btn btn-primary"><i class="bi bi-github"></i> Kode Sumber</a>
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Tutup</button>
      </div>
    </div>
  </div>
</div>
"""
odoo_modal = BeautifulSoup(odoo_modal_html, 'html.parser')
footer = soup.find('footer', id='contact')
footer.insert_after(odoo_modal)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
