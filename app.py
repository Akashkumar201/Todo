
from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///posts.db'
db=SQLAlchemy(app)
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return 'Blog Post'+str(self.id)


all_posts=[]
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts',methods=['GET','POST'])
def post():
    if request.method=='POST':
        post_title=request.form['title']
  
        new_post=BlogPost(title=post_title)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        all_posts=BlogPost.query.all()  
    return render_template('base.html',posts=all_posts)
@app.route('/posts/delete/<int:id>')
def delete(id):
    post=BlogPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/posts')



if __name__=="__main__":
    app.run(debug=True)