---
title: Publications
type: page
cms_exclude: false
view: citation
---

<script>
document.addEventListener('DOMContentLoaded', function() {
  var items = document.querySelectorAll('.pub-list-item');
  var years = new Set();
  items.forEach(function(item) {
    var m = item.textContent.match(/\(?(20[12][0-9])\)?/);
    if (m) { years.add(m[1]); }
  });
  var sorted = Array.from(years).sort().reverse();
  var container = document.querySelector('.pub-list-item')?.parentElement;
  if (!container || sorted.length === 0) return;
  var filterDiv = document.createElement('div');
  filterDiv.id = 'year-filter';
  filterDiv.style.cssText = 'display:flex;flex-wrap:wrap;gap:0.5rem;justify-content:center;margin:1.5rem 0 2rem;';
  var allBtn = document.createElement('button');
  allBtn.textContent = 'All';
  allBtn.className = 'inline-flex items-center rounded-md border border-gray-300 bg-white px-3 py-1.5 text-sm font-medium text-gray-700 hover:bg-gray-50 dark:border-gray-500 dark:bg-gray-800 dark:text-gray-300';
  allBtn.dataset.year = 'all';
  allBtn.style.background = '#f97316';
  allBtn.style.color = '#fff';
  filterDiv.appendChild(allBtn);
  sorted.forEach(function(y, i) {
    var btn = document.createElement('button');
    btn.textContent = y;
    btn.className = 'inline-flex items-center rounded-md border border-gray-300 bg-white px-3 py-1.5 text-sm font-medium text-gray-700 hover:bg-gray-50 dark:border-gray-500 dark:bg-gray-800 dark:text-gray-300';
    btn.dataset.year = y;
    filterDiv.appendChild(btn);
  });
  container.insertBefore(filterDiv, container.firstChild);
  var btns = filterDiv.querySelectorAll('button');
  btns.forEach(function(btn) {
    btn.addEventListener('click', function() {
      var selected = btn.dataset.year;
      btns.forEach(function(b) {
        b.style.background = selected === b.dataset.year ? '#f97316' : '';
        b.style.color = selected === b.dataset.year ? '#fff' : '';
      });
      items.forEach(function(item) {
        var m = item.textContent.match(/\(?(20[12][0-9])\)?/);
        var y = m ? m[1] : '';
        item.style.display = (selected === 'all' || y === selected) ? '' : 'none';
      });
    });
  });
});
</script>
