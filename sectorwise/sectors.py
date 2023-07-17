from bs4 import BeautifulSoup
def somesector():
 html = '''<select class="dropdown__select" name="sector" data-dashlane-rid="7a8103c7c775aec0" data-form-type="other">
<option value="">Select...</option>
<option value="0819">MODARABAS</option>
<option value="0803">CABLE &amp; ELECTRICAL GOODS</option>
<option value="0820">OIL &amp; GAS EXPLORATION COMPANIES</option>
<option value="0826">SUGAR &amp; ALLIED INDUSTRIES</option>
<option value="0829">TEXTILE COMPOSITE</option>
<option value="0808">ENGINEERING</option>
<option value="0825">REFINERY</option>
<option value="0831">TEXTILE WEAVING</option>
<option value="0806">CLOSE - END MUTUAL FUND</option>
<option value="0813">INV. BANKS / INV. COS. / SECURITIES COS.</option>
<option value="0821">OIL &amp; GAS MARKETING COMPANIES</option>
<option value="0811">GLASS &amp; CERAMICS</option>
<option value="0835">WOOLLEN</option>
<option value="0824">POWER GENERATION &amp; DISTRIBUTION</option>
<option value="0804">CEMENT</option>
<option value="0832">TOBACCO</option>
<option value="0827">SYNTHETIC &amp; RAYON</option>
<option value="0816">LEATHER &amp; TANNERIES</option>
<option value="0828">TECHNOLOGY &amp; COMMUNICATION</option>
<option value="0823">PHARMACEUTICALS</option>
<option value="0801">AUTOMOBILE ASSEMBLER</option>
<option value="0833">TRANSPORT</option>
<option value="0807">COMMERCIAL BANKS</option>
<option value="0814">JUTE</option>
<option value="0838">PROPERTY</option>
<option value="0805">CHEMICAL</option>
<option value="0834">VANASPATI &amp; ALLIED INDUSTRIES</option>
<option value="0818">MISCELLANEOUS</option>
<option value="0836">REAL ESTATE INVESTMENT TRUST</option>
<option value="0837">EXCHANGE TRADED FUNDS</option>
<option value="0830">TEXTILE SPINNING</option>
<option value="0815">LEASING COMPANIES</option>
<option value="0810">FOOD &amp; PERSONAL CARE PRODUCTS</option>
<option value="0802">AUTOMOBILE PARTS &amp; ACCESSORIES</option>
<option value="0812">INSURANCE</option>
<option value="0822">PAPER &amp; BOARD</option>
<option value="0809">FERTILIZER</option>
</select>'''

 soup = BeautifulSoup(html, 'html.parser')
 select_element = soup.find('select', {'name': 'sector'})

 names = []
 found = False

 for option in select_element.find_all('option'):
    if found:
        names.append(option.get_text(strip=True))
    if option['value'] == '0830':  # Value for "TEXTILE SPINNING"
        found = True

 return names

def sectorsshare():
    pic='https://imgtr.ee/image/jG1br'
    return pic
#somesector()
def indicesshare():
    pic='https://imgtr.ee/image/jGQrC'
    return pic

def numberofshare():
    pic='https://imgtr.ee/image/jGdRG'
    return pic
