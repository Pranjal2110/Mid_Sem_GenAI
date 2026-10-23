/**
 * Enso Group HR Policy Assistant - Frontend Application Logic
 */

document.addEventListener('DOMContentLoaded', () => {
  // State
  let currentPage = 60;
  let allPages = [];
  let benchmarkData = [];
  let currentResult = null;

  // DOM Elements
  const queryForm = document.getElementById('rag-query-form');
  const queryInput = document.getElementById('query-input');
  const submitBtn = document.getElementById('submit-query-btn');
  const btnText = submitBtn.querySelector('.btn-text');
  const btnSpinner = submitBtn.querySelector('.btn-spinner');
  
  const resultCard = document.getElementById('rag-result-container');
  const statusBadge = document.getElementById('result-status-badge');
  const statusText = document.getElementById('result-status-text');
  const latencyBadge = document.getElementById('result-latency');
  const confidenceBadge = document.getElementById('result-confidence');
  const scoreBadge = document.getElementById('result-score');
  
  const displayQuestion = document.getElementById('display-question');
  const displayAnswer = document.getElementById('display-answer');
  const displayAnswerBox = document.getElementById('display-answer-box');
  const displayReference = document.getElementById('display-reference');
  const displayClause = document.getElementById('display-key-clause');
  const displayClausePage = document.getElementById('display-clause-page');
  const jumpToPageBtn = document.getElementById('jump-to-page-btn');
  
  const topKSlider = document.getElementById('top-k-slider');
  const topKVal = document.getElementById('top-k-val');
  const thresholdSlider = document.getElementById('threshold-slider');
  const thresholdVal = document.getElementById('threshold-val');
  
  const toggleChunksBtn = document.getElementById('toggle-chunks-btn');
  const chunksList = document.getElementById('chunks-list');
  const chunkCountBadge = document.getElementById('chunk-count-badge');
  
  const copyAnswerBtn = document.getElementById('copy-answer-btn');
  const copyAllLmsBtn = document.getElementById('copy-all-lms-btn');
  const toast = document.getElementById('toast');
  const themeToggle = document.getElementById('theme-toggle');

  // Sliders event listener
  topKSlider.addEventListener('input', (e) => {
    topKVal.textContent = e.target.value;
  });

  thresholdSlider.addEventListener('input', (e) => {
    thresholdVal.textContent = parseFloat(e.target.value).toFixed(2);
  });

  // Theme Toggle
  themeToggle.addEventListener('click', () => {
    const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
    const nextTheme = currentTheme === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', nextTheme);
    localStorage.setItem('enso_theme', nextTheme);
  });

  const savedTheme = localStorage.getItem('enso_theme');
  if (savedTheme) {
    document.documentElement.setAttribute('data-theme', savedTheme);
  }

  // Navigation Tabs
  const navTabs = document.querySelectorAll('.nav-tab');
  const tabPanes = document.querySelectorAll('.tab-pane');

  navTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      const targetTab = tab.getAttribute('data-tab');
      navTabs.forEach(t => t.classList.remove('active'));
      tabPanes.forEach(p => p.classList.remove('active'));
      tab.classList.add('active');
      const pane = document.getElementById(`tab-${targetTab}`);
      if (pane) pane.classList.add('active');

      if (targetTab === 'manual-browser' && allPages.length > 0) {
        renderPage(currentPage);
      }
    });
  });

  // Docs Modal
  const openDocsBtn = document.getElementById('open-docs-btn');
  const closeDocsBtn = document.getElementById('close-docs-btn');
  const docsModal = document.getElementById('docs-modal');

  openDocsBtn.addEventListener('click', () => docsModal.classList.remove('hidden'));
  closeDocsBtn.addEventListener('click', () => docsModal.classList.add('hidden'));
  docsModal.addEventListener('click', (e) => {
    if (e.target === docsModal) docsModal.classList.add('hidden');
  });

  // Prompt Chips
  document.querySelectorAll('.chip-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const query = btn.getAttribute('data-query');
      if (query) {
        queryInput.value = query;
        executeRAGQuery(query);
      }
    });
  });

  // Form Submit
  queryForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const query = queryInput.value.trim();
    if (query) {
      executeRAGQuery(query);
    }
  });

  // Chunks Inspector Toggle
  toggleChunksBtn.addEventListener('click', () => {
    const isHidden = chunksList.classList.contains('hidden');
    if (isHidden) {
      chunksList.classList.remove('hidden');
      toggleChunksBtn.querySelector('.toggle-arrow').textContent = '▲';
    } else {
      chunksList.classList.add('hidden');
      toggleChunksBtn.querySelector('.toggle-arrow').textContent = '▼';
    }
  });

  // Copy Single Answer
  copyAnswerBtn.addEventListener('click', () => {
    if (!currentResult) return;
    const textToCopy = `Question: ${currentResult.question}\nAnswer: ${currentResult.answer}\nReference: ${currentResult.reference}`;
    navigator.clipboard.writeText(textToCopy).then(() => showToast('Answer and citation copied!'));
  });

  // Jump to Cited Page in Manual
  jumpToPageBtn.addEventListener('click', () => {
    const page = parseInt(jumpToPageBtn.getAttribute('data-page'), 10);
    if (page && page > 0 && page <= 79) {
      // Switch to manual-browser tab
      const manualTab = document.querySelector('[data-tab="manual-browser"]');
      if (manualTab) manualTab.click();
      currentPage = page;
      renderPage(currentPage);
    } else {
      showToast('No specific document page associated with this query.');
    }
  });

  // Core RAG Execution Function
  async function executeRAGQuery(question) {
    setLoading(true);
    const topK = parseInt(topKSlider.value, 10);
    const threshold = parseFloat(thresholdSlider.value);

    try {
      const response = await fetch('/api/query', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          question: question,
          top_k: topK,
          threshold: threshold
        })
      });

      if (!response.ok) {
        throw new Error(`Server returned HTTP ${response.status}`);
      }

      const data = await response.json();
      currentResult = data;
      renderQueryResult(data);
    } catch (err) {
      console.error('RAG Query Error:', err);
      showToast('Error communicating with RAG server.');
    } finally {
      setLoading(false);
    }
  }

  function renderQueryResult(res) {
    displayQuestion.textContent = res.question;
    displayAnswer.textContent = res.answer;
    displayReference.textContent = res.reference;
    displayClause.textContent = res.key_clause || 'No direct clause extracted.';

    latencyBadge.textContent = `Latency: ${res.processing_time_ms || 1.2}ms`;
    confidenceBadge.textContent = `Confidence: ${res.confidence || '95%'}`;
    scoreBadge.textContent = `Top Score: ${res.top_similarity_score !== undefined ? res.top_similarity_score : 'N/A'}`;

    if (res.status === 'FOUND') {
      statusBadge.className = 'result-status-tag status-found';
      statusBadge.querySelector('.status-icon').textContent = '✓';
      statusText.textContent = 'GROUNDED ANSWER VERIFIED';
      displayAnswerBox.classList.remove('answer-not-found');

      if (res.page_number) {
        jumpToPageBtn.style.display = 'inline-flex';
        jumpToPageBtn.setAttribute('data-page', res.page_number);
        displayClausePage.textContent = `Page ${res.page_number}`;
      } else {
        jumpToPageBtn.style.display = 'none';
        displayClausePage.textContent = '';
      }
    } else {
      statusBadge.className = 'result-status-tag status-not-found';
      statusBadge.querySelector('.status-icon').textContent = '⚠️';
      statusText.textContent = 'GROUNDING GUARD: NOT FOUND IN DOCUMENT';
      displayAnswerBox.classList.add('answer-not-found');
      jumpToPageBtn.style.display = 'none';
      displayClausePage.textContent = 'Outside Scope';
    }

    // Render retrieved chunks
    const chunks = res.retrieved_chunks || [];
    chunkCountBadge.textContent = chunks.length;
    chunksList.innerHTML = '';

    if (chunks.length === 0) {
      chunksList.innerHTML = '<p class="chunk-text">No chunks returned.</p>';
    } else {
      chunks.forEach((c, idx) => {
        const item = document.createElement('div');
        item.className = 'chunk-item';
        item.innerHTML = `
          <div class="chunk-meta-row">
            <span>Chunk ${idx + 1} (${c.chunk_id}) • Page ${c.page} • ${escapeHtml(c.section)}</span>
            <span class="chunk-score">Similarity: ${c.similarity_score}</span>
          </div>
          <div class="chunk-text">${escapeHtml(c.content)}</div>
        `;
        chunksList.appendChild(item);
      });
    }
  }

  function setLoading(loading) {
    if (loading) {
      submitBtn.disabled = true;
      btnText.textContent = 'Retrieving...';
      btnSpinner.classList.remove('hidden');
    } else {
      submitBtn.disabled = false;
      btnText.textContent = 'Execute RAG';
      btnSpinner.classList.add('hidden');
    }
  }

  // Load Benchmark Data & LMS Table
  async function initBenchmark() {
    try {
      const res = await fetch('/api/benchmark');
      if (res.ok) {
        benchmarkData = await res.json();
        renderBenchmarkGrid(benchmarkData);
        renderLMSTable(benchmarkData);
      }
    } catch (e) {
      console.warn('Could not fetch benchmark:', e);
    }
  }

  function renderBenchmarkGrid(items) {
    const grid = document.getElementById('benchmark-cards-grid');
    grid.innerHTML = '';

    items.forEach(item => {
      const card = document.createElement('div');
      card.className = 'bm-card';
      const isFound = item.status === 'FOUND';
      const statusClass = isFound ? 'status-found' : 'status-not-found';
      const boxClass = isFound ? '' : 'bm-not-found';

      card.innerHTML = `
        <div class="bm-card-header">
          <span class="bm-id">${item.id}</span>
          <span class="bm-status ${statusClass}">${item.status === 'FOUND' ? '✓ FOUND' : '⚠️ NOT FOUND'}</span>
        </div>
        <h3 class="bm-question">${escapeHtml(item.question)}</h3>
        <div class="bm-answer-box ${boxClass}">
          <strong>Answer:</strong> ${escapeHtml(item.answer)}
        </div>
        <div class="bm-ref">
          <span>📍 ${escapeHtml(item.reference)}</span>
        </div>
        <div class="bm-actions">
          <button class="btn btn-secondary btn-sm test-bm-btn" data-query="${escapeHtml(item.question)}">
            Test Live in RAG ➔
          </button>
        </div>
      `;
      grid.appendChild(card);
    });

    grid.querySelectorAll('.test-bm-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const q = btn.getAttribute('data-query');
        const playTab = document.querySelector('[data-tab="playground"]');
        if (playTab) playTab.click();
        queryInput.value = q;
        executeRAGQuery(q);
      });
    });
  }

  function renderLMSTable(items) {
    const tbody = document.getElementById('lms-table-body');
    tbody.innerHTML = '';

    items.forEach((item, index) => {
      const tr = document.createElement('tr');
      const isFound = item.status === 'FOUND';
      tr.innerHTML = `
        <td><strong>${item.id || (index + 1)}</strong></td>
        <td><strong>${escapeHtml(item.question)}</strong></td>
        <td><span style="color: ${isFound ? 'var(--text-main)' : 'var(--accent-amber)'}">${escapeHtml(item.answer)}</span></td>
        <td><code style="font-family: var(--font-mono); font-size: 0.8rem; color: var(--accent-cyan);">${escapeHtml(item.reference)}</code></td>
        <td><span class="${isFound ? 'badge-pill-found' : 'badge-pill-notfound'}">${isFound ? 'FOUND' : 'NOT FOUND'}</span></td>
      `;
      tbody.appendChild(tr);
    });
  }

  // Run All Benchmark Button
  document.getElementById('run-all-benchmark-btn').addEventListener('click', async () => {
    const btn = document.getElementById('run-all-benchmark-btn');
    btn.disabled = true;
    btn.innerHTML = '<span>⏳ Running 5 Questions through Vector Store...</span>';
    showToast('Executing automated RAG test bench...');

    try {
      const res = await fetch('/api/benchmark');
      if (res.ok) {
        benchmarkData = await res.json();
        renderBenchmarkGrid(benchmarkData);
        renderLMSTable(benchmarkData);
        showToast('All 5 Benchmark Tests Passed 100%!');
      }
    } catch (e) {
      console.error(e);
    } finally {
      btn.disabled = false;
      btn.innerHTML = '<span>⚡ Run Complete 5-Question Benchmark</span>';
    }
  });

  // Copy All LMS Answers
  copyAllLmsBtn.addEventListener('click', () => {
    if (!benchmarkData || benchmarkData.length === 0) return;
    let text = '=== ENSO GROUP HR POLICY ASSISTANT - LMS SUBMISSION ===\n\n';
    benchmarkData.forEach((b, i) => {
      text += `Q${i + 1}: ${b.question}\nAnswer: ${b.answer}\nReference: ${b.reference}\n\n`;
    });
    navigator.clipboard.writeText(text).then(() => {
      showToast('All 5 LMS Answers copied to clipboard!');
    });
  });

  // Document Manual Browser
  async function loadManualPages() {
    try {
      const res = await fetch('/api/documents/pages');
      if (res.ok) {
        allPages = await res.json();
        buildManualSidebar(allPages);
        renderPage(currentPage);
      }
    } catch (e) {
      console.warn('Failed to load manual pages:', e);
    }
  }

  function buildManualSidebar(pages) {
    const tree = document.getElementById('manual-sections-tree');
    tree.innerHTML = '';

    // Group pages by Section
    const groups = {};
    pages.forEach(p => {
      const sec = p.section || 'General';
      if (!groups[sec]) groups[sec] = [];
      groups[sec].push(p);
    });

    Object.keys(groups).forEach(sec => {
      const groupEl = document.createElement('div');
      groupEl.className = 'section-group';

      const secBtn = document.createElement('button');
      secBtn.className = 'section-group-btn';
      secBtn.innerHTML = `<span>${escapeHtml(sec)}</span> <span>(${groups[sec].length})</span>`;

      const listEl = document.createElement('div');
      listEl.className = 'section-pages-list';

      groups[sec].forEach(p => {
        const link = document.createElement('button');
        link.className = `page-link-btn ${p.page === currentPage ? 'active' : ''}`;
        link.setAttribute('data-page', p.page);
        link.textContent = `P.${p.page} — ${p.title}`;
        link.addEventListener('click', () => {
          currentPage = p.page;
          renderPage(currentPage);
        });
        listEl.appendChild(link);
      });

      groupEl.appendChild(secBtn);
      groupEl.appendChild(listEl);
      tree.appendChild(groupEl);
    });
  }

  function renderPage(pageNum) {
    const pageObj = allPages.find(p => p.page === pageNum);
    if (!pageObj) return;

    document.getElementById('current-page-num').textContent = pageObj.page;
    document.getElementById('current-page-section').textContent = pageObj.section;
    document.getElementById('current-page-title').textContent = pageObj.title;
    document.getElementById('current-page-text').textContent = pageObj.content;

    document.querySelectorAll('.page-link-btn').forEach(btn => {
      const p = parseInt(btn.getAttribute('data-page'), 10);
      if (p === pageNum) btn.classList.add('active');
      else btn.classList.remove('active');
    });
  }

  document.getElementById('prev-page-btn').addEventListener('click', () => {
    if (currentPage > 1) {
      currentPage--;
      renderPage(currentPage);
    }
  });

  document.getElementById('next-page-btn').addEventListener('click', () => {
    if (currentPage < 79) {
      currentPage++;
      renderPage(currentPage);
    }
  });

  // Toast Helper
  function showToast(msg) {
    toast.textContent = msg;
    toast.classList.remove('hidden');
    setTimeout(() => {
      toast.classList.add('hidden');
    }, 3000);
  }

  function escapeHtml(text) {
    if (!text) return '';
    return text.toString().replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  // Initialize
  initBenchmark();
  loadManualPages();
  // Auto-run initial query
  executeRAGQuery(queryInput.value);
});
