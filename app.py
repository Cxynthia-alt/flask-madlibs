
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story


app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)


@app.route('/form')
def add_innput():
    return render_template('form.html')


@app.route('/output')
def show_output():
    place_name = request.args.get("place")
    noun = request.args.get("noun")
    verb = request.args.get("verb")
    adjective = request.args.get("adjective")
    plural_noun = request.args.get("plural_noun")
    story = Story(["place", "noun", "verb", "adjective", "plural_noun"],
                  'Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. It loved to {verb} {plural_noun}.')
    answers = {"place": place_name, "noun": noun, "verb": verb,
               "adjective": adjective, "plural_noun": plural_noun}
    output_text = story.generate(answers)
    test = 'this is a test'
    return render_template("output.html", output_text=output_text, test=test)
