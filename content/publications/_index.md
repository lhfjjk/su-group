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
  var select = document.createElement('select');
  select.id = 'year-filter';
  select.style.cssText = 'display:block;width:220px;margin:0 auto 2rem;text-align:center;padding:0.4rem 0.75rem;border:1px solid #d1d5db;border-radius:0.375rem;font-size:0.9rem;cursor:pointer;';
  var opt0 = document.createElement('option');
  opt0.value = 'all'; opt0.textContent = '— All Years —';
  select.appendChild(opt0);
  sorted.forEach(function(y) {
    var opt = document.createElement('option');
    opt.value = y; opt.textContent = y;
    select.appendChild(opt);
  });
  container.insertBefore(select, container.firstChild);
  select.addEventListener('change', function() {
    var selected = select.value;
    items.forEach(function(item) {
      var m = item.textContent.match(/\(?(20[12][0-9])\)?/);
      var y = m ? m[1] : '';
      item.style.display = (selected === 'all' || y === selected) ? '' : 'none';
    });
  });
});
</script>
