#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-rubygems-tasks
Version  : 0.2.4
Release  : 6
URL      : https://rubygems.org/downloads/rubygems-tasks-0.2.4.gem
Source0  : https://rubygems.org/downloads/rubygems-tasks-0.2.4.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-rdoc

%description
# rubygems-tasks
* [Source](https://github.com/postmodern/rubygems-tasks)
* [Issues](https://github.com/postmodern/rubygems-tasks/issues)
* [Email](mailto:postmodern.mod3 at gmail.com)

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n rubygems-tasks-0.2.4
gem spec %{SOURCE0} -l --ruby > rubygem-rubygems-tasks.gemspec

%build
gem build rubygem-rubygems-tasks.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
rubygems-tasks-0.2.4.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/rubygems-tasks-0.2.4.gem
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/.document
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/.rspec
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/.yardopts
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/ChangeLog.md
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/LICENSE.txt
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/README.md
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/gemspec.yml
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/build.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/build/gem.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/build/tar.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/build/task.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/build/zip.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/console.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/install.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/printing.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/project.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/push.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/release.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/scm.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/scm/push.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/scm/status.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/scm/tag.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/sign.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/sign/checksum.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/sign/pgp.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/sign/task.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/task.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/tasks.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/rubygems-tasks.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/spec/console_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/spec/install_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/spec/project_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/spec/push_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/spec/rake_context.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/spec/scm/push_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/spec/scm/status_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/spec/scm/tag_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/spec/sign/pgp_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/rubygems-tasks-0.2.4/spec/tasks_spec.rb
/usr/lib64/ruby/gems/2.3.0/specifications/rubygems-tasks-0.2.4.gemspec
