---
title: ''
summary: ''
date: 2022-10-24
type: landing

design:
  spacing: '6rem'

sections:
  - block: resume-biography-3
    content:
      username: su-weiping
      text: ''
      headings:
        about: 'About Our Group'
        education: 'Education'
        interests: ''
    design:
      background:
        gradient_mesh:
          enable: true
      name:
        size: lg
      avatar:
        size: large
        shape: circle
  - block: markdown
    content:
      title: 'Research'
      subtitle: 'Our research focuses on green organic synthesis and C-H functionalization'
      text: |-
        Our group is dedicated to developing novel synthetic methods in organic chemistry, with particular emphasis on:
        - Transition metal-catalyzed C-H functionalization
        - Photocatalytic synthesis
        - Dehydrogenative coupling reactions
        Sustainable and green chemistry approaches
  - block: team-showcase
    content:
      title: Our Team
      subtitle: World-class researchers advancing organic synthesis
      text: ''
      user_groups:
        - Principal Investigators
        - Postdoctoral Researchers
        - PhD Students
        - Alumni
      sort_by: weight
      sort_ascending: true
    design:
      show_role: true
      show_organizations: true
      show_interests: false
      max_columns: 4
      show_social: true
      show_empty_groups: false
  - block: collection
    id: publications
    content:
      title: Selected Publications
      filters:
        folders:
          - publications
      count: 10
    design:
      view: citation
  - block: cta-card
    content:
      title: Contact Us
      text: |-
        Institute of Chemistry, Chinese Academy of Sciences
        Email: contact@fjirsm.ac.cn
    design:
      card:
        css_class: 'bg-primary-300 dark:bg-primary-700'
---
