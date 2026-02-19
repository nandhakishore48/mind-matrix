/* ═══════════════════════════════════════════════════════════
   BrandCraft — Shared JavaScript Utilities
   Theme toggle, auth, API wrapper, sidebar, toasts
   ═══════════════════════════════════════════════════════════ */

const API_BASE = 'http://localhost:8000/api';

// ─── Theme Toggle ───
function initTheme() {
    const saved = localStorage.getItem('theme') || 'dark';
    document.documentElement.setAttribute('data-theme', saved);
}

function toggleTheme() {
    const current = document.documentElement.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
}

// ─── Auth Helpers ───
function getToken() {
    return localStorage.getItem('token');
}

function setToken(token) {
    localStorage.setItem('token', token);
}

function removeToken() {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
}

function getUser() {
    const u = localStorage.getItem('user');
    return u ? JSON.parse(u) : null;
}

function setUser(user) {
    localStorage.setItem('user', JSON.stringify(user));
}

function isLoggedIn() {
    return !!getToken();
}

function requireAuth() {
    if (!isLoggedIn()) {
        window.location.href = 'login.html';
        return false;
    }
    return true;
}

function requireAdmin() {
    const user = getUser();
    if (!user || user.role !== 'admin') {
        window.location.href = 'dashboard.html';
        return false;
    }
    return true;
}

function logout() {
    removeToken();
    window.location.href = 'index.html';
}

// ─── API Wrapper ───
async function api(endpoint, options = {}) {
    const url = `${API_BASE}${endpoint}`;
    const headers = {
        'Content-Type': 'application/json',
        ...options.headers,
    };

    const token = getToken();
    if (token) {
        headers['Authorization'] = `Bearer ${token}`;
    }

    try {
        const response = await fetch(url, {
            ...options,
            headers,
        });

        if (response.status === 401) {
            removeToken();
            window.location.href = 'login.html';
            return null;
        }

        // Get response text first to handle empty responses
        const text = await response.text();

        if (!text) {
            // Empty response body
            if (!response.ok) {
                throw new Error(`HTTP Error: ${response.status} ${response.statusText}`);
            }
            return null;
        }

        const data = JSON.parse(text);

        if (!response.ok) {
            throw new Error(data.detail || 'API Error');
        }

        return data;
    } catch (error) {
        console.error('API Error:', error);
        throw error;
    }
}

// ─── Toast Notifications ───
function showToast(message, type = 'success') {
    const existing = document.querySelector('.toast');
    if (existing) existing.remove();

    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    toast.textContent = message;
    document.body.appendChild(toast);

    setTimeout(() => toast.remove(), 3500);
}

// ─── Loading Spinner ───
function showSpinner(id) {
    const el = document.getElementById(id);
    if (el) el.classList.add('active');
}

function hideSpinner(id) {
    const el = document.getElementById(id);
    if (el) el.classList.remove('active');
}

// ─── Sidebar Renderer ───
function renderSidebar(activePage) {
    const user = getUser();
    const sidebar = document.getElementById('sidebar');
    if (!sidebar) return;

    const navItems = [
        { section: 'Main' },
        { icon: '📊', label: 'Dashboard', href: 'dashboard.html', id: 'dashboard' },
        { section: 'AI Tools' },
        { icon: '✨', label: 'Brand Names', href: 'brand-name.html', id: 'brand-name' },
        { icon: '🎨', label: 'Logo Generator', href: 'logo-generator.html', id: 'logo-generator' },
        { icon: '🏗️', label: 'Brand Identity', href: 'brand-identity.html', id: 'brand-identity' },
        { icon: '📝', label: 'Content Generator', href: 'content-generator.html', id: 'content-generator' },
        { icon: '📈', label: 'Sentiment Analysis', href: 'sentiment-analysis.html', id: 'sentiment-analysis' },
        { icon: '🤖', label: 'AI Assistant', href: 'assistant.html', id: 'assistant' },
        { section: 'Manage' },
        { icon: '📁', label: 'Brand Kit', href: 'brand-kit.html', id: 'brand-kit' },
    ];

    if (user && user.role === 'admin') {
        navItems.push({ section: 'Admin' });
        navItems.push({ icon: '⚙️', label: 'Admin Panel', href: 'admin.html', id: 'admin' });
    }

    let html = `
        <div class="sidebar-brand">
            <div class="logo-icon">B</div>
            <span>BrandCraft</span>
        </div>
        <ul class="sidebar-nav">
    `;

    navItems.forEach(item => {
        if (item.section) {
            html += `<li class="sidebar-section">${item.section}</li>`;
        } else {
            const active = activePage === item.id ? 'active' : '';
            html += `
                <li>
                    <a href="${item.href}" class="${active}">
                        <span class="nav-icon">${item.icon}</span>
                        ${item.label}
                    </a>
                </li>
            `;
        }
    });

    html += `
        </ul>
        <div style="padding: 20px 24px; margin-top: auto; border-top: 1px solid rgba(255,255,255,0.08);">
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px;">
                <div style="width: 36px; height: 36px; border-radius: 50%; background: var(--accent-gradient); display: flex; align-items: center; justify-content: center; color: white; font-weight: 700; font-size: 0.85rem;">
                    ${user ? user.username.charAt(0).toUpperCase() : 'U'}
                </div>
                <div>
                    <div style="font-size: 0.85rem; font-weight: 600; color: #e8e8f0;">${user ? user.username : 'User'}</div>
                    <div style="font-size: 0.7rem; color: #6868a0;">${user ? user.role : 'user'}</div>
                </div>
            </div>
            <div style="display: flex; gap: 8px;">
                <button class="btn btn-sm btn-secondary" onclick="toggleTheme()" style="flex:1; font-size: 0.75rem;">🌓 Theme</button>
                <button class="btn btn-sm btn-danger" onclick="logout()" style="flex:1; font-size: 0.75rem;">Logout</button>
            </div>
        </div>
    `;

    sidebar.innerHTML = html;
}

// ─── Mobile Sidebar Toggle ───
function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    if (sidebar) sidebar.classList.toggle('open');
}

// ─── Format Date ───
function formatDate(dateStr) {
    const d = new Date(dateStr);
    return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
}

// ─── Markdown-like rendering ───
function renderMarkdown(text) {
    if (!text) return '';
    return text
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
        .replace(/\*(.*?)\*/g, '<em>$1</em>')
        .replace(/^### (.*$)/gm, '<h4>$1</h4>')
        .replace(/^## (.*$)/gm, '<h3>$1</h3>')
        .replace(/^# (.*$)/gm, '<h2>$1</h2>')
        .replace(/^[-•] (.*$)/gm, '<li>$1</li>')
        .replace(/(<li>.*<\/li>)/gs, '<ul>$1</ul>')
        .replace(/\n/g, '<br>');
}

// ─── Init on every page ───
document.addEventListener('DOMContentLoaded', () => {
    initTheme();
});
