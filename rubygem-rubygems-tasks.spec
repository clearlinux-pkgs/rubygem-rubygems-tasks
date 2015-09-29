#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-rubygems-tasks
Version  : 0.2.4
Release  : 4
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
gem_dir=$(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .${gem_dir} \
--bindir .%{_bindir} \
rubygems-tasks-0.2.4.gem

mkdir -p %{buildroot}${gem_dir}
cp -pa .${gem_dir}/* \
%{buildroot}${gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/rubygems-tasks-0.2.4.gem
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Build/Gem/build-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Build/Gem/cdesc-Gem.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Build/Gem/define-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Build/Gem/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Build/Tar/build-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Build/Tar/cdesc-Tar.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Build/Tar/define-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Build/Tar/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Build/Task/build-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Build/Task/build_task-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Build/Task/cdesc-Task.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Build/Zip/build-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Build/Zip/cdesc-Zip.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Build/Zip/define-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Build/Zip/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Build/cdesc-Build.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Console/cdesc-Console.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Console/command-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Console/console-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Console/define-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Console/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Console/options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Install/cdesc-Install.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Install/define-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Install/install-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Install/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Printing/cdesc-Printing.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Printing/debug-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Printing/error-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Printing/fu_output_message-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Printing/status-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Project/builds-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Project/bundler%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Project/cdesc-Project.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Project/directories-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Project/gemspec-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Project/gemspecs-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Project/name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Project/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Project/primary_gemspec-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Project/root-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Project/scm-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Push/cdesc-Push.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Push/define-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Push/host-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Push/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Push/push-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Release/cdesc-Release.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Release/define-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Release/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/SCM/Push/cdesc-Push.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/SCM/Push/define-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/SCM/Push/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/SCM/Push/push%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/SCM/Status/cdesc-Status.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/SCM/Status/define-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/SCM/Status/dirty%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/SCM/Status/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/SCM/Status/status-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/SCM/Tag/cdesc-Tag.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/SCM/Tag/define-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/SCM/Tag/format-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/SCM/Tag/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/SCM/Tag/sign%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/SCM/Tag/sign-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/SCM/Tag/tag%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/SCM/Tag/version_tag-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/SCM/cdesc-SCM.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Sign/Checksum/cdesc-Checksum.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Sign/Checksum/define-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Sign/Checksum/md5%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Sign/Checksum/md5-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Sign/Checksum/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Sign/Checksum/sha1%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Sign/Checksum/sha1-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Sign/Checksum/sha2%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Sign/Checksum/sha2-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Sign/Checksum/sha512%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Sign/Checksum/sha512-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Sign/Checksum/sign-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Sign/PGP/cdesc-PGP.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Sign/PGP/define-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Sign/PGP/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Sign/PGP/sign-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Sign/Task/cdesc-Task.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Sign/Task/sign-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Sign/Task/sign_task-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Sign/cdesc-Sign.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Task/bundle-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Task/cdesc-Task.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Task/gem-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Task/gemspec_tasks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Task/invoke-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Task/multi_task-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Task/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Task/project-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Task/run-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/Task/task%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/build-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/cdesc-Tasks.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/console-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/install-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/push-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/release-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/scm-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/Tasks/sign-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/Gem/cdesc-Gem.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/page-ChangeLog_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/page-LICENSE_txt.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubygems-tasks-0.2.4/ri/page-README_md.ri
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/.document
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/.gitignore
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/.rspec
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/.yardopts
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/ChangeLog.md
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/LICENSE.txt
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/README.md
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/gemspec.yml
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks.rb
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/build.rb
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/build/gem.rb
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/build/tar.rb
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/build/task.rb
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/build/zip.rb
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/console.rb
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/install.rb
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/printing.rb
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/project.rb
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/push.rb
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/release.rb
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/scm.rb
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/scm/push.rb
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/scm/status.rb
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/scm/tag.rb
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/sign.rb
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/sign/checksum.rb
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/sign/pgp.rb
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/sign/task.rb
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/task.rb
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/lib/rubygems/tasks/tasks.rb
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/rubygems-tasks.gemspec
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/spec/console_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/spec/install_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/spec/project_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/spec/push_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/spec/rake_context.rb
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/spec/scm/push_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/spec/scm/status_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/spec/scm/tag_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/spec/sign/pgp_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.2.0/gems/rubygems-tasks-0.2.4/spec/tasks_spec.rb
/usr/lib64/ruby/gems/2.2.0/specifications/rubygems-tasks-0.2.4.gemspec
