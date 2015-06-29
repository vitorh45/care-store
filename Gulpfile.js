// Aqui nós carregamos o gulp e os plugins através da função `require` do nodejs
var gulp = require('gulp');
var jshint = require('gulp-jshint');
var uglify = require('gulp-uglify');
var concat = require('gulp-concat');
var rename = require('gulp-rename');
var jasmine = require('gulp-jasmine');
 
// Definimos o diretorio dos arquivos para evitar repetição futuramente
var files = "./src/*.js";
var tests_files = "./src/test/*.js";
 
//Aqui criamos uma nova tarefa através do ´gulp.task´ e damos a ela o nome 'lint'
gulp.task('lint', function() {
	gulp.src(files).pipe(jshint()).pipe(jshint.reporter('default'));
});
 
//Criamos outra tarefa com o nome 'dist'
gulp.task('dist', function() {
	gulp.src(files).pipe(concat('./dist')).pipe(rename('dist.min.js')).pipe(uglify()).pipe(gulp.dest('./dist'));
});

gulp.task('specs', function () {
    return gulp.src(tests_files).pipe(jasmine());
});

gulp.task('default', function() {
	gulp.run('lint', 'dist');
	gulp.watch(files, function(evt) {
		gulp.run('lint', 'dist');
	});
});