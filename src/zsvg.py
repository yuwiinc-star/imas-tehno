def zsvg_light():
    s=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300" fill="none" stroke="#6B6A66" stroke-width="1.5"><rect width="400" height="300" fill="#FFFFFF" stroke="none"/>']
    s.append('<path d="M60,246 H236 V54 H360" stroke="#161616" stroke-width="2"/><path d="M60,214 H204 V86 H360" stroke="#161616" stroke-width="2"/>')
    s.append('<rect x="44" y="214" width="16" height="32"/><rect x="360" y="54" width="16" height="32"/><path d="M60,230 H220 V70 H360" stroke="#9C9C98" stroke-dasharray="3 5"/>')
    b=lambda x,y: f'<path d="M{x-11},{y-6} h22 l-4,12 h-14 z" fill="#C8352B" stroke="none"/>'
    for x in range(84,205,30): s.append(b(x,230))
    for y in range(200,90,-30): s.append(b(220,y))
    for x in range(250,360,30): s.append(b(x,70))
    s.append('<rect x="372" y="40" width="18" height="26" fill="#E8E8E6"/><circle cx="381" cy="53" r="5"/><path d="M70,186 h44 l-8,28 h-28 z" fill="#E8E8E6"/><path d="M92,150 v36" stroke="#161616"/>')
    s.append('<path d="M60,270 H236" stroke="#9C9C98"/><path d="M60,266 v8 M236,266 v8" stroke="#9C9C98"/><text x="148" y="286" fill="#6B6A66" font-family="JetBrains Mono, monospace" font-size="10" text-anchor="middle" stroke="none">L ПО ЗАКАЗУ</text>')
    s.append('<path d="M20,246 V54" stroke="#9C9C98"/><path d="M16,246 h8 M16,54 h8" stroke="#9C9C98"/><text x="14" y="150" fill="#6B6A66" font-family="JetBrains Mono, monospace" font-size="10" text-anchor="middle" transform="rotate(-90 14 150)" stroke="none">H ПО ЗАКАЗУ</text>')
    s.append('<text x="300" y="20" fill="#6B6A66" font-family="JetBrains Mono, monospace" font-size="10" text-anchor="middle" stroke="none">Z-ВЕРСИЯ · КОВШИ 250/420 ММ</text></svg>')
    return "".join(s)

def zsvg_dark():
    return zsvg_light().replace('<rect width="400" height="300" fill="#FFFFFF" stroke="none"/>','').replace('stroke="#161616"','stroke="#F2F2F0"').replace('stroke="#6B6A66"','stroke="#9C9C98"').replace('fill="#E8E8E6"','fill="#2A2C2B"').replace('fill="#6B6A66"','fill="#9C9C98"')
