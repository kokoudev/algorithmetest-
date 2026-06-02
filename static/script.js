/* ==========================================
   ALGOVISUALIZER CORE JAVASCRIPT LOGIC
   ========================================== */

document.addEventListener('DOMContentLoaded', () => {
    checkApiStatus();
});

// --- API STATUS CHECK ---
function checkApiStatus() {
    const statusDot = document.querySelector('#api-status .status-dot');
    const statusText = document.querySelector('#api-status .status-text');
    const statusBadge = document.getElementById('api-status');

    fetch('/api/health')
        .then(response => response.json())
        .then(data => {
            if (data.status === 'ok') {
                statusBadge.classList.add('online');
                statusText.textContent = 'API Connecté';
            } else {
                statusBadge.classList.add('offline');
                statusText.textContent = 'Erreur API';
            }
        })
        .catch(() => {
            statusBadge.classList.add('offline');
            statusText.textContent = 'API Hors-ligne';
        });
}

// --- TAB SWITCHER ---
function switchTab(tabId) {
    // Supprimer la classe active de tous les onglets
    document.querySelectorAll('.tab-pane').forEach(pane => pane.classList.remove('active'));
    document.querySelectorAll('.nav-item').forEach(item => item.classList.remove('active'));

    // Ajouter la classe active à l'onglet sélectionné
    document.getElementById(tabId).classList.add('active');
    document.querySelector(`.nav-item[data-tab="${tabId}"]`).classList.add('active');
}

// --- PRESET GENERATORS ---
function generateRandomArray(inputId, size, min, max) {
    const arr = [];
    for (let i = 0; i < size; i++) {
        arr.push(Math.floor(Math.random() * (max - min + 1)) + min);
    }
    document.getElementById(inputId).value = arr.join(' ');
}

function generateSortedArray(inputId, size) {
    const arr = [];
    for (let i = 0; i < size; i++) {
        arr.push(i * 3 + Math.floor(Math.random() * 3));
    }
    document.getElementById(inputId).value = arr.join(' ');
}

function generateReversedArray(inputId, size) {
    const arr = [];
    for (let i = size; i > 0; i--) {
        arr.push(i * 3 + Math.floor(Math.random() * 3));
    }
    document.getElementById(inputId).value = arr.join(' ');
}

function generateRandomTwoSum(inputId, size) {
    const arr = [];
    for (let i = 0; i < size; i++) {
        // Mélanger des grands et petits nombres positifs et négatifs
        const val = Math.floor(Math.random() * 30000) - 15000;
        arr.push(val);
    }
    document.getElementById(inputId).value = arr.join(' ');
}

function generateTwoSumMatching(inputId) {
    // Génère des nombres qui s'associent pour former des sommes dans l'intervalle [-10000, 10000]
    const arr = [];
    for (let i = 1; i <= 20; i++) {
        arr.push(i * 400); // Ex: 400, 800, 1200...
        arr.push(-i * 400 + Math.floor(Math.random() * 50)); // Ex: -380, -780...
    }
    document.getElementById(inputId).value = arr.join(' ');
}

function generateBigNumbers(digits) {
    let numA = '';
    let numB = '';
    
    // Générer le premier chiffre (différent de 0)
    numA += Math.floor(Math.random() * 9) + 1;
    numB += Math.floor(Math.random() * 9) + 1;
    
    for (let i = 1; i < digits; i++) {
        numA += Math.floor(Math.random() * 10);
        numB += Math.floor(Math.random() * 10);
    }
    
    document.getElementById('ka-input-a').value = numA;
    document.getElementById('ka-input-b').value = numB;
}

function clearInput(inputId) {
    document.getElementById(inputId).value = '';
}

// --- ALGORITHME 1 : QUICKSORT ---
function runQuickSort() {
    const numbers = document.getElementById('qs-input').value.trim();
    const strategy = document.getElementById('qs-strat').value;
    const loader = document.getElementById('qs-loading');
    const resultCard = document.getElementById('qs-result');
    const chartContainer = document.getElementById('qs-chart');

    if (!numbers) {
        alert('Veuillez entrer des nombres.');
        return;
    }

    loader.style.display = 'block';
    resultCard.style.display = 'none';

    fetch('/api/quicksort', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ numbers, strategy })
    })
    .then(res => res.json())
    .then(data => {
        loader.style.display = 'none';
        if (data.success) {
            // Affichage des statistiques
            document.getElementById('qs-stat-comps').textContent = data.comparaisons;
            document.getElementById('qs-stat-strat').textContent = data.strategy;
            
            // Affichage des tableaux
            document.getElementById('qs-orig-val').textContent = `[${numbers.split(/\s+/).join(', ')}]`;
            document.getElementById('qs-sorted-val').textContent = `[${data.sorted_array.join(', ')}]`;
            
            // Construction du graphique
            chartContainer.innerHTML = '';
            const maxVal = Math.max(...data.sorted_array);
            const minVal = Math.min(...data.sorted_array);
            const range = maxVal - minVal || 1;
            
            // On limite la visualisation à 25 éléments pour des raisons esthétiques
            const elementsToDraw = data.sorted_array.slice(0, 25);
            
            elementsToDraw.forEach(val => {
                const bar = document.createElement('div');
                bar.className = 'chart-bar';
                bar.setAttribute('data-value', val);
                
                // Normaliser la hauteur entre 10% et 100%
                const pct = ((val - minVal) / range) * 90 + 10;
                bar.style.height = `${pct}%`;
                chartContainer.appendChild(bar);
            });

            resultCard.style.display = 'block';
        } else {
            alert('Erreur : ' + data.error);
        }
    })
    .catch(err => {
        loader.style.display = 'none';
        alert('Erreur réseau lors de la communication avec le serveur.');
    });
}

// --- ALGORITHME 2 : TWO SUM ---
let lastFoundSums = []; // Variable globale pour stocker les sommes courantes (pour filtrage)

function runTwoSum() {
    const numbers = document.getElementById('ts-input').value.trim();
    const loader = document.getElementById('ts-loading');
    const resultCard = document.getElementById('ts-result');
    const sumsList = document.getElementById('ts-sums-list');
    const searchInput = document.getElementById('ts-search');

    if (!numbers) {
        alert('Veuillez entrer une liste de nombres.');
        return;
    }

    loader.style.display = 'block';
    resultCard.style.display = 'none';
    searchInput.value = '';

    fetch('/api/two-sum', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ numbers })
    })
    .then(res => res.json())
    .then(data => {
        loader.style.display = 'none';
        if (data.success) {
            document.getElementById('ts-stat-count').textContent = data.count;
            lastFoundSums = data.sums;
            
            renderSumsList(data.sums);
            
            // Gérer la note de limite
            const limitNote = document.getElementById('ts-limit-note');
            if (data.total_sums > 100) {
                limitNote.textContent = `Affichage des 100 premières sommes (sur ${data.total_sums} au total).`;
                limitNote.style.display = 'block';
            } else {
                limitNote.style.display = 'none';
            }

            resultCard.style.display = 'block';
        } else {
            alert('Erreur : ' + data.error);
        }
    })
    .catch(err => {
        loader.style.display = 'none';
        alert('Erreur réseau.');
    });
}

function renderSumsList(sums) {
    const sumsList = document.getElementById('ts-sums-list');
    sumsList.innerHTML = '';
    
    if (sums.length === 0) {
        sumsList.innerHTML = '<p class="text-muted" style="width: 100%; text-align: center; padding: 20px;">Aucune somme trouvée.</p>';
        return;
    }
    
    sums.forEach(sum => {
        const tag = document.createElement('span');
        tag.className = 'sum-tag';
        tag.textContent = sum;
        sumsList.appendChild(tag);
    });
}

function filterSums() {
    const query = document.getElementById('ts-search').value.trim();
    if (!query) {
        renderSumsList(lastFoundSums);
        return;
    }
    
    const filtered = lastFoundSums.filter(sum => sum.toString().includes(query));
    renderSumsList(filtered);
}

// --- ALGORITHME 3 : KARATSUBA ---
function runKaratsuba() {
    const aVal = document.getElementById('ka-input-a').value.trim();
    const bVal = document.getElementById('ka-input-b').value.trim();
    const loader = document.getElementById('ka-loading');
    const resultCard = document.getElementById('ka-result');

    if (!aVal || !bVal) {
        alert('Veuillez entrer les deux nombres.');
        return;
    }

    const a = parseInt(aVal, 10);
    const b = parseInt(bVal, 10);

    if (isNaN(a) || isNaN(b) || a < 0 || b < 0) {
        alert('Veuillez entrer des nombres entiers positifs valides.');
        return;
    }

    loader.style.display = 'block';
    resultCard.style.display = 'none';

    fetch('/api/karatsuba', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ a, b })
    })
    .then(res => res.json())
    .then(data => {
        loader.style.display = 'none';
        if (data.success) {
            // Remplir les résultats
            document.getElementById('ka-std-res').textContent = formatBigNumberString(data.verification.toString());
            document.getElementById('ka-res').textContent = formatBigNumberString(data.result.toString());
            
            // Badge de vérification
            const badge = document.getElementById('ka-match-badge');
            if (data.correct) {
                badge.textContent = 'Vérifié ✅';
                badge.className = 'verification-badge';
                badge.style.background = 'rgba(16, 185, 129, 0.15)';
                badge.style.color = '#10b981';
            } else {
                badge.textContent = 'Erreur ❌';
                badge.style.background = 'rgba(239, 68, 68, 0.15)';
                badge.style.color = '#ef4444';
            }
            
            // Calculer et afficher les étapes du premier niveau de division
            const aStr = a.toString();
            const bStr = b.toString();
            const n = Math.max(aStr.length, bStr.length);
            const m = Math.floor(n / 2);
            const D = Math.pow(10, m);
            
            const high_a = Math.floor(a / D);
            const low_a = a % D;
            const high_b = Math.floor(b / D);
            const low_b = b % D;
            
            const e1 = high_a * high_b;
            const e2 = low_a * low_b;
            const e3 = (high_a + low_a) * (high_b + low_b);
            const e4 = e3 - e1 - e2;
            
            document.getElementById('ka-math-a-split').innerHTML = `A<sub>high</sub> = <strong>${high_a}</strong>, A<sub>low</sub> = <strong>${low_a}</strong> <span class="text-muted">(split à 10<sup>${m}</sup> = ${D})</span>`;
            document.getElementById('ka-math-b-split').innerHTML = `B<sub>high</sub> = <strong>${high_b}</strong>, B<sub>low</sub> = <strong>${low_b}</strong>`;
            
            document.getElementById('ka-math-e1').innerHTML = `${high_a} × ${high_b} = <strong>${e1}</strong>`;
            document.getElementById('ka-math-e2').innerHTML = `${low_a} × ${low_b} = <strong>${e2}</strong>`;
            document.getElementById('ka-math-e3').innerHTML = `(${high_a} + ${low_a}) × (${high_b} + ${low_b}) = ${high_a + low_a} × ${high_b + low_b} = <strong>${e3}</strong>`;
            document.getElementById('ka-math-e4').innerHTML = `${e3} - ${e1} - ${e2} = <strong>${e4}</strong>`;
            
            const formulaDisplay = `${e1} × 10<sup>${2*m}</sup> + ${e4} × 10<sup>${m}</sup> + ${e2} = <strong>${data.result}</strong>`;
            document.getElementById('ka-math-final').innerHTML = formulaDisplay;

            resultCard.style.display = 'block';
        } else {
            alert('Erreur : ' + data.error);
        }
    })
    .catch(err => {
        loader.style.display = 'none';
        alert('Erreur réseau.');
    });
}

function formatBigNumberString(str) {
    // Ajoute des séparateurs de milliers pour l'affichage de grands nombres
    if (str.length <= 4) return str;
    return str.replace(/\B(?=(\d{3})+(?!\d))/g, " ");
}
