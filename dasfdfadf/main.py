from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import create_session
import global_init
from data.users import User
from data.jobs import Jobs


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mars_explorer.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def works_log():
    jobs = db.session.query(Jobs).all()
    works = []
    for job in jobs:
        leader = User.query.get(job.team_leader)
        works.append({
            'id': job.id,
            'title': job.job,
            'leader': f"{leader.surname} {leader.name}",
            'duration': f"{job.work_size} hours",
            'collaborators': job.collaborators,
            'is_finished': "Yes" if job.is_finished else "No"
        })
    return render_template('works_log.html', works=works)

if __name__ == '__main__':
    app.run(debug=True)
