<?php

use Symfony\Component\DependencyInjection\Argument\RewindableGenerator;

// This file has been auto-generated by the Symfony Dependency Injection Component for internal use.
// Returns the private 'templating.finder' shared service.

return $this->services['templating.finder'] = new \Symfony\Bundle\FrameworkBundle\CacheWarmer\TemplateFinder(${($_ = isset($this->services['kernel']) ? $this->services['kernel'] : $this->get('kernel', 1)) && false ?: '_'}, ${($_ = isset($this->services['templating.filename_parser']) ? $this->services['templating.filename_parser'] : ($this->services['templating.filename_parser'] = new \Symfony\Bundle\FrameworkBundle\Templating\TemplateFilenameParser())) && false ?: '_'}, ($this->targetDirs[3].'/app/Resources'));
