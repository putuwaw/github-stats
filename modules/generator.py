BG_DARK = "#000000"
BG_LIGHT = "#FFFFFF"
TITLE_DARK = "#FFFFFF"
TITLE_LIGHT = "#3B82F6"
TITLE_DANGER = "#EF4444"
STATS_DARK = "#CBD5E1"
STATS_LIGHT = "#1E293B"
BORDER_COLOR = "#1E293B"
ICON_LIGHT = "#000000"
ICON_DARK = "#3B82F6"


REPO_ICON = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16" height="16"><path class="icon" d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path></svg>'''
STARS_ICON = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16" height="16"><path class="icon" d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Zm0 2.445L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75 0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456-.53-3.084a.75.75 0 0 1 .216-.664l2.24-2.183-3.096-.45a.75.75 0 0 1-.564-.41L8 2.694Z"></path></svg>'''
FORKS_ICON = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16" height="16"><path class="icon" d="M5 5.372v.878c0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75v-.878a2.25 2.25 0 1 1 1.5 0v.878a2.25 2.25 0 0 1-2.25 2.25h-1.5v2.128a2.251 2.251 0 1 1-1.5 0V8.5h-1.5A2.25 2.25 0 0 1 3.5 6.25v-.878a2.25 2.25 0 1 1 1.5 0ZM5 3.25a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Zm6.75.75a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Zm-3 8.75a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Z"></path></svg>'''
PR_ICON = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16" height="16"><path class="icon" d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path></svg>'''
COMMIT_ICON = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16" height="16"><path class="icon" d="M11.93 8.5a4.002 4.002 0 0 1-7.86 0H.75a.75.75 0 0 1 0-1.5h3.32a4.002 4.002 0 0 1 7.86 0h3.32a.75.75 0 0 1 0 1.5Zm-1.43-.75a2.5 2.5 0 1 0-5 0 2.5 2.5 0 0 0 5 0Z"></path></svg>'''


def formatter(number: int) -> str:
    if number >= 100_000:
        return str(number // 1000) + "k"
    elif number >= 10_000:
        return str(number // 1000) + "." + str(number % 1000)[0] + "k"
    return str(number)


def get_style_svg(theme):
    titleColor = TITLE_DARK if theme == "dark" else TITLE_LIGHT
    statsColor = STATS_DARK if theme == "dark" else STATS_LIGHT
    iconColor = ICON_DARK if theme == "dark" else ICON_LIGHT
    return '''
        <style>
            .title {{
                font: 800 1.25rem Sans-Serif;
                fill: {};
            }}
                
            .stats {{
                font: 600 14px Sans-Serif; 
                fill: {};
            }}
            .icon {{
                fill: {};
            }}
        </style>
    '''.format(titleColor, statsColor, iconColor)


def get_border_svg(theme):
    bgColor = BG_DARK if theme == "dark" else BG_LIGHT
    return '''
      <rect rx=".375rem" height="100%" stroke="{}" width="370" fill="{}" stroke-opacity=".2"/>
    '''.format(BORDER_COLOR, bgColor)


def get_title_svg(username):
    return '''<g transform="translate(25, 35)">
            <g transform="translate(0, 0)">
                <text class="title">{}</text>
            </g>
        </g>'''.format(username)


def get_stats_svg(repo, stars, forks, pr, commit):
    stats = {"Total Public Repository": (repo, REPO_ICON), "Total Stars Earned": (stars, STARS_ICON),
             "Total Forks Earned": (forks, FORKS_ICON), "Total Merged PRs": (pr, PR_ICON), "Total Commit": (commit, COMMIT_ICON)}
    posY = 0

    result = '''
                <g transform="translate(0, 55)">
                    <svg>
            '''
    for key, value in stats.items():
        result += '''
                    <g transform="translate(0, {})">
                        <g transform="translate(25, 0)">
                            {}
                            <text class="stats" x="27" y="12.5">{}:</text>
                            <text class="stats" x="240" y="12.5">{}</text>
                        </g>
                    </g>'''.format(posY, value[1], key, formatter(value[0]))
        posY += 25
    result += '''
                    </svg>
                </g>
            '''
    return result


def get_svg(name, username, repo, stars, forks, pr, commit, theme):
    result = ""
    result += '''
                <svg width="370" height="200" xmlns="http://www.w3.org/2000/svg"> 
                <title>GitHub Stats | @{}</title>
            '''.format(username)
    result += get_style_svg(theme)
    result += get_border_svg(theme)
    result += get_title_svg(name)
    result += get_stats_svg(repo, stars, forks, pr, commit)
    result += '''</svg>'''
    return result


def get_error(title, message):
    return '''
        <svg width="370" height="200" xmlns="http://www.w3.org/2000/svg"> 
            <title>GitHub Stats | ERROR</title>
            <style>
                .title {{
                    font: 800 1.25rem Sans-Serif;
                    fill: {};
                }}
                    
                .message {{
                    font: 600 14px Sans-Serif; 
                    fill: {};
                }}
            </style>
            <rect rx=".375rem" height="100%" stroke="{}" width="370" fill="{}" stroke-opacity="10"/>
            <g transform="translate(25, 35)">
                <g transform="translate(0, 0)">
                    <text class="title">{}</text>
                </g>
                <g transform="translate(0, 25)">
                    <text class="message">{}</text>
                </g>
            </g>
        </svg>
    '''.format(TITLE_DANGER, STATS_LIGHT, BORDER_COLOR, BG_LIGHT, title, message)
