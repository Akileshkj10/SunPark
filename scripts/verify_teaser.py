from pypdf import PdfReader

r = PdfReader(r'deliverables\SunPark_Investment_Teaser.pdf')
text = ''.join(p.extract_text() or '' for p in r.pages)
tl = text.lower()

checks = {
    'GBP 260K present':              '260K' in text,
    'GBP 262K removed':              '262K' not in text,
    'Gross margin ~86%':             '86%' in text and '86.5' not in text,
    '~2 Years payback':              ('2' in text and 'Equity Payback' in text),
    '4 Years removed':               '4 Years' not in text,
    'GBP 2.2M contracted revenue':   '2.2M' in text,
    'IRR removed':                   'IRR' not in text,
    'Local Installer in table':      'Local' in text,
    'Ind. PPA column':               'Ind.' in text,
    'PPA financing row':             'PPA financing' in text,
    'Multi-site rollout row':        'Multi-site' in text,
    'IFC removed':                   'IFC' not in text,
    '52% renewable removed':         '52 percent' not in tl and '52%' not in text,
    '760 kWp removed':               '760' not in text,
    'SR500 still present':           'SR500' in text,
    '18.9% CAGR present':            '18.9' in text,
    'Finance Act VAT bullet':        'Finance Act' in text,
    'Discount rate removed':         'Discount' not in text,
    'GBP 2.6M cap still present':    '2.6M' in text,
    'GBP 420K still present':        '420' in text,
}

ok = all(checks.values())
for k, v in checks.items():
    status = 'PASS' if v else 'FAIL'
    print(f'[{status}] {k}')
print()
print('All checks passed!' if ok else 'SOME CHECKS FAILED - review above')
