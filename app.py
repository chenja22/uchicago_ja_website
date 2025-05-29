from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    slides = [
      'event1.jpg',
      'event2.jpg',
      'event3.jpg',
      'event4.jpg',
      'event5.jpg',
      'event6.jpg',
    ]
    return render_template('home.html', slides=slides)

@app.route('/links')
def links():
    return render_template('links.html')

@app.route('/impact')
def impact():
    stats = {
        'students': '300+',
        'volunteers': '60',
        'schools': ['South Shore HS', 'Martha Ruggles STEM', 'Clara Barton ES', 'Ashburn Community ES', 'Washington Irving ES'],
        'alumni_goals': '90%',
        'alumni_literacy': '84%',
        'report_url': '#'  # Optional link to Alumni Impact Report
    }
    return render_template('impact.html', stats=stats)

@app.route('/team')
def team():
    members = [
        {'name': 'Jack Wells', 'title': 'Founder and President', 'photo': 'jack_wells.jpg'},
        {'name': 'Louis Nahon', 'title': 'Recruitment Director', 'photo': 'louis_nahon.jpg'},
        {'name': 'Samara Blatt', 'title': 'Communications', 'photo': 'samara_blatt.jpg'},
        {'name': 'Aly Elkaffas', 'title': 'Internal Ops', 'photo': 'aly_elkaffas.jpg'},
        {'name': 'Roger Li', 'title': 'Internal Ops', 'photo': 'roger_li.jpg'},
        {'name': 'Arsene Cherpion', 'title': 'Treasurer', 'photo': 'arsene_cherpion.jpg'},
        {'name': 'Eitan Fischer', 'title': 'Marketing', 'photo': 'eitan_fischer.jpg'},
        {'name': 'Jarrett Chen', 'title': 'Marketing', 'photo': 'jarrett_chen.jpg'},
        {'name': 'Lal Koyuncu', 'title': 'Onboarding', 'photo': 'lal_koyuncu.jpg'},
        {'name': 'Maia Lewis', 'title': 'Onboarding', 'photo': 'maia_lewis.jpg'},
        {'name': 'Sean Lim', 'title': 'Outreach', 'photo': 'sean_lim.jpg'},
        {'name': 'Ben Luo', 'title': 'Compliance', 'photo': 'ben_luo.jpg'}
    ]
    return render_template('team.html', members=members)

@app.route('/join')
def join():
    return render_template('join.html')

@app.route('/member')
def member():
    # Placeholder for member-only content or protected route
    return render_template('member.html')

if __name__ == '__main__':
    app.run(debug=True)